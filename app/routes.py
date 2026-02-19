import csv
import io
import json
import random

from flask import (
    Blueprint,
    Response,
    current_app,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from .grading import grade_submission
from .models import Attempt, db
from .physics import generate_problem

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    if session.get("user_code"):
        return redirect(url_for("main.problem"))
    return render_template("index.html")


@bp.post("/set_user")
def set_user():
    user_code = request.form.get("user_code", "").strip()
    if not user_code:
        return render_template("index.html", error="Please enter a user code.")
    session["user_code"] = user_code
    return redirect(url_for("main.problem"))


@bp.get("/change_user")
def change_user():
    session.clear()
    return redirect(url_for("main.index"))


@bp.get("/problem")
def problem():
    if not session.get("user_code"):
        return redirect(url_for("main.index"))

    seed = random.randint(1, 2**31 - 1)
    config = generate_problem(seed)
    session["current_problem"] = config
    return render_template("problem.html", config=config, user_code=session["user_code"])


@bp.post("/submit")
def submit():
    if not session.get("user_code"):
        return redirect(url_for("main.index"))

    config = session.get("current_problem")
    if not config:
        return redirect(url_for("main.problem"))

    try:
        submitted_ex = float(request.form.get("submitted_ex", ""))
        submitted_ey = float(request.form.get("submitted_ey", ""))
    except ValueError:
        return render_template(
            "problem.html",
            config=config,
            user_code=session["user_code"],
            error="Please enter valid numeric values for Ex and Ey.",
        )

    tol = float(current_app.config["DEFAULT_TOL_PERCENT"])
    result = grade_submission(
        submitted_ex,
        submitted_ey,
        config["correct_ex"],
        config["correct_ey"],
        tol,
    )

    attempt = Attempt(
        user_code=session["user_code"],
        seed=config["seed"],
        config_json=json.dumps(config),
        submitted_ex=submitted_ex,
        submitted_ey=submitted_ey,
        correct_ex=config["correct_ex"],
        correct_ey=config["correct_ey"],
        tol_percent=tol,
        ex_correct=result["ex_correct"],
        ey_correct=result["ey_correct"],
        score=result["score"],
    )
    db.session.add(attempt)
    db.session.commit()

    return render_template(
        "result.html",
        result=result,
        attempt=attempt,
        correct_ex=config["correct_ex"],
        correct_ey=config["correct_ey"],
        user_code=session["user_code"],
        tol=tol,
    )


@bp.get("/history")
def history():
    if not session.get("user_code"):
        return redirect(url_for("main.index"))

    attempts = (
        Attempt.query.filter_by(user_code=session["user_code"])
        .order_by(Attempt.created_at.desc())
        .all()
    )
    return render_template("history.html", attempts=attempts, user_code=session["user_code"])


@bp.get("/admin/export.csv")
def export_csv():
    token = request.args.get("token", "")
    if not current_app.config.get("ADMIN_TOKEN") or token != current_app.config["ADMIN_TOKEN"]:
        return Response("Unauthorized", status=401)

    attempts = Attempt.query.order_by(Attempt.created_at.asc()).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(
        [
            "id",
            "user_code",
            "created_at",
            "seed",
            "config_json",
            "submitted_ex",
            "submitted_ey",
            "correct_ex",
            "correct_ey",
            "tol_percent",
            "ex_correct",
            "ey_correct",
            "score",
        ]
    )

    for a in attempts:
        writer.writerow(
            [
                a.id,
                a.user_code,
                a.created_at.isoformat(),
                a.seed,
                a.config_json,
                a.submitted_ex,
                a.submitted_ey,
                a.correct_ex,
                a.correct_ey,
                a.tol_percent,
                a.ex_correct,
                a.ey_correct,
                a.score,
            ]
        )

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=attempts.csv"},
    )
