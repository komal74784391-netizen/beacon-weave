"""Mesh clock synchronisation primitives."""

from dataclasses import dataclass
from statistics import mean
from typing import List


@dataclass
class Beacon:
    node: str
    skew_ms: float
    weight: float = 1.0


def robust_offset(beacons: List[Beacon]) -> float:
    if not beacons:
        return 0.0
    total_weight = sum(b.weight for b in beacons)
    if total_weight == 0:
        return mean([b.skew_ms for b in beacons])
    return sum(b.skew_ms * b.weight for b in beacons) / total_weight


def corrected_clock(current_ms: int, asymmetry_ms: float, offset_ms: float) -> int:
    return int(current_ms + offset_ms - asymmetry_ms / 2)
