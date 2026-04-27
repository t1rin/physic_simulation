from typing import List

from .strength import Strength


class Point():
    def __init__(self, mass: float, radius: float, coordinates: List[float]):
        self.mass: float = mass
        self.radius: float = radius
        self.coordinates: List[float] = None
        self.strengths: List[Strength] = []