import math

def mount_offset(seat, vehicle):
    """乘客局部偏移。"""
    raise NotImplementedError("TODO: mount_offset")

def clear_velocity(velocity):
    """下车清速度。"""
    raise NotImplementedError("TODO: clear_velocity")

def ignore_mutual(mounted):
    """挂载互碰忽略。"""
    raise NotImplementedError("TODO: ignore_mutual")

def apply_root(pos, delta, applied):
    """根运动只应用一次。"""
    raise NotImplementedError("TODO: apply_root")

def world_transform(local, parent):
    """世界变换。"""
    raise NotImplementedError("TODO: world_transform")

def detach_before_destroy(mounted):
    """销毁先卸载。"""
    raise NotImplementedError("TODO: detach_before_destroy")

def seat_of(seats, passenger_id):
    """按 ID 找座。"""
    raise NotImplementedError("TODO: seat_of")

def speed_allows(speed, limit):
    """按当前速度判定。"""
    raise NotImplementedError("TODO: speed_allows")

def sync_local(local):
    """同步乘客局部。"""
    raise NotImplementedError("TODO: sync_local")

def fallback_point(point, occupied):
    """后备下车点。"""
    raise NotImplementedError("TODO: fallback_point")

def attach_key(child, parent):
    """挂载键。"""
    raise NotImplementedError("TODO: attach_key")

def local_of(world, parent):
    """局部坐标。"""
    raise NotImplementedError("TODO: local_of")

def is_seated(state):
    """乘坐状态。"""
    raise NotImplementedError("TODO: is_seated")

def clamp_speed(value, limit):
    """速度钳制。"""
    raise NotImplementedError("TODO: clamp_speed")

def seat_key(vehicle, seat):
    """座位键。"""
    raise NotImplementedError("TODO: seat_key")
