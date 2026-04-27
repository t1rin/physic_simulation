from typing import List

from .point import Point
from .polygon import Polygon
from .strength import Strength


class Body():
    def __init__(self, mass: float, material_point: Point):
        self.mass: float = mass
        self.material_point: Point = material_point
        self.polygons: List[Polygon] = []
        self.strengths: List[Strength] = []