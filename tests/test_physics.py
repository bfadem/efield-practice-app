import pytest
import importlib.util
from pathlib import Path


spec = importlib.util.spec_from_file_location("physics", Path("app/physics.py"))
physics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(physics)


def independent_field(config):
    target = config["charges"][0]
    tx = target["x"] * physics.GRID_SPACING_M
    ty = target["y"] * physics.GRID_SPACING_M
    ex = ey = 0.0
    for src in config["charges"][1:]:
        sx = src["x"] * physics.GRID_SPACING_M
        sy = src["y"] * physics.GRID_SPACING_M
        rx = tx - sx
        ry = ty - sy
        r = (rx**2 + ry**2) ** 0.5
        q_c = src["q_nc"] * physics.NANOCOULOMB_TO_COULOMB
        ex += physics.K_COULOMB * q_c * rx / (r**3)
        ey += physics.K_COULOMB * q_c * ry / (r**3)
    return ex, ey


def test_fixed_seed_solver_matches_independent_calculation():
    config = physics.generate_problem(20240219)
    ex, ey = independent_field(config)
    assert config["correct_ex"] == pytest.approx(ex)
    assert config["correct_ey"] == pytest.approx(ey)
