import importlib.util
from pathlib import Path


spec = importlib.util.spec_from_file_location("grading", Path("app/grading.py"))
grading = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grading)


def test_within_tolerance_and_partial_credit():
    result = grading.grade_submission(
        sub_ex=102.0,
        sub_ey=80.0,
        corr_ex=100.0,
        corr_ey=100.0,
        tol_percent=3.0,
    )
    assert result["ex_correct"] is True
    assert result["ey_correct"] is False
    assert result["score"] == 1.0


def test_scientific_notation_float_parsing_example():
    value = float("3.2e4")
    assert value == 32000.0
