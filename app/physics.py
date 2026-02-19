import random
from dataclasses import dataclass

K_COULOMB = 8.9875517923e9
GRID_SPACING_M = 0.10
NANOCOULOMB_TO_COULOMB = 1e-9


@dataclass(frozen=True)
class Charge:
    x: int
    y: int
    q_nc: int


def generate_problem(seed: int):
    rng = random.Random(seed)
    charges = [
        Charge(rng.choice([1, 2]), rng.choice([1, 2]), rng.choice([-3, -2, -1, 1, 2, 3])),
        Charge(-rng.choice([1, 2]), rng.choice([1, 2]), rng.choice([-3, -2, -1, 1, 2, 3])),
        Charge(-rng.choice([1, 2]), -rng.choice([1, 2]), rng.choice([-3, -2, -1, 1, 2, 3])),
        Charge(rng.choice([1, 2]), -rng.choice([1, 2]), rng.choice([-3, -2, -1, 1, 2, 3])),
    ]
    target = charges[0]
    ex, ey = field_at_target(target, charges[1:])
    return {
        "seed": seed,
        "charges": [charge.__dict__ for charge in charges],
        "target": {"x": target.x, "y": target.y},
        "correct_ex": ex,
        "correct_ey": ey,
    }


def field_at_target(target: Charge, source_charges: list[Charge]):
    ex = 0.0
    ey = 0.0

    target_x_m = target.x * GRID_SPACING_M
    target_y_m = target.y * GRID_SPACING_M

    for src in source_charges:
        sx_m = src.x * GRID_SPACING_M
        sy_m = src.y * GRID_SPACING_M

        rx = target_x_m - sx_m
        ry = target_y_m - sy_m
        r_sq = rx**2 + ry**2
        r = r_sq**0.5

        q_c = src.q_nc * NANOCOULOMB_TO_COULOMB
        factor = K_COULOMB * q_c / (r**3)
        ex += factor * rx
        ey += factor * ry

    return ex, ey
