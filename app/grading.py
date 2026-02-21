def within_percent_tolerance(submitted: float, correct: float, tol_percent: float) -> bool:
    if correct == 0:
        return abs(submitted) <= (tol_percent / 100.0)
    return abs(submitted - correct) <= abs(correct) * (tol_percent / 100.0)

def within_abs_tolerance(submitted: float, correct: float, tol_abs: float) -> bool:
    return abs(submitted - correct) <= tol_abs

def angle_diff_deg(a: float, b: float) -> float:
    # Smallest absolute difference, accounting for wrap at 360 degrees.
    return abs((a - b + 180.0) % 360.0 - 180.0)

def grade_submission(
    sub_ex: float,
    sub_ey: float,
    sub_mag: float,
    sub_theta_deg: float,
    corr_ex: float,
    corr_ey: float,
    corr_mag: float,
    corr_theta_deg: float,
    tol_percent: float,
    tol_theta_deg: float,
):
    ex_correct = within_percent_tolerance(sub_ex, corr_ex, tol_percent)
    ey_correct = within_percent_tolerance(sub_ey, corr_ey, tol_percent)
    mag_correct = within_percent_tolerance(sub_mag, corr_mag, tol_percent)
    theta_correct = angle_diff_deg(sub_theta_deg, corr_theta_deg) <= tol_theta_deg
    score = float(ex_correct) + float(ey_correct) + float(mag_correct) + float(theta_correct)
    return {
        "ex_correct": ex_correct,
        "ey_correct": ey_correct,
        "mag_correct": mag_correct,
        "theta_correct": theta_correct,
        "score": score,
    }
