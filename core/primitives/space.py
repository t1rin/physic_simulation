from typing import List

from .body import Body
from .strength import Strength


class Space():
    def __init__(self, dimensionality):
        self.dimensionality: int = dimensionality
        self.bodies: List[Body] = []
        self.strengths: List[Strength] = []