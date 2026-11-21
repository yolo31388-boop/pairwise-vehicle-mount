import pytest
import math
from gameplay import vehicle_mount as mod

CASES = [
    ("offset", 'm.mount_offset((1, 1, 1), (10, 0, 0)) == (-9, 1, 1)'),
    ("velocity", 'm.clear_velocity((1, 2, 3)) == (0, 0, 0)'),
    ("mutual", 'm.ignore_mutual(True) is True'),
    ("root_once", 'm.apply_root((1, 1, 1), (2, 0, 0), True) == (1, 1, 1)'),
    ("root_apply", 'm.apply_root((1, 1, 1), (2, 0, 0), False) == (3, 1, 1)'),
    ("world", 'm.world_transform((1, 1, 1), (2, 2, 2)) == (3, 3, 3)'),
    ("destroy", 'm.detach_before_destroy(True) is False'),
    ("seat", 'm.seat_of(["a", "b"], "b") == 1'),
    ("speed", 'm.speed_allows(2, 2) is True'),
    ("sync", 'm.sync_local((1, 2, 3)) == (1, 2, 3)'),
    ("fallback", 'm.fallback_point((1, 1, 1), True) == (1, 2, 1)'),
    ("attach", 'm.attach_key("p", "car") == "p@car"'),
    ("local", 'm.local_of((3, 3, 3), (1, 1, 1)) == (2, 2, 2)'),
    ("seated", 'm.is_seated("seated") is True'),
    ("clamp", 'm.clamp_speed(5, 3) == 3')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
