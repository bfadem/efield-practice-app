def within_percent_tolerance(submitted: float, correct: float, tol_percent: float) -> bool:
    if correct == 0:
        return abs(submitted) <= (tol_percent / 100.0)
    return abs(submitted - correct) <= abs(correct) * (tol_percent / 100.0)


def grade_submission(sub_ex: float, sub_ey: float, corr_ex: float, corr_ey: float, tol_percent: float):
    ex_correct = within_percent_tolerance(sub_ex, corr_ex, tol_percent)
    ey_correct = within_percent_tolerance(sub_ey, corr_ey, tol_percent)
    score = float(ex_correct) + float(ey_correct)
    return {
        "ex_correct": ex_correct,
        "ey_correct": ey_correct,
        "score": score,
    }
