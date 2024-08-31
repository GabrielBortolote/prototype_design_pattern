from typing import List
from point import Point
from prototype import Prototype

class GeometricalForm(Prototype):
    def __init__(self, points: List[Point]=[], clone: "GeometricalForm"=None):
        self.points = points
        # cloning
        if clone:
            for point in clone.points:
                self.point.append(point)

    def clone(self):
        return self.__class__(clone=self)
    
    def __str__(self):
        return '\n'.join([str(point) for point in self.points])
        
    
