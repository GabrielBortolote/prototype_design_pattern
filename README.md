# Prototype

This project implements a use case for a Design Pattern, the Prototype. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/prototype).

## What it is?

Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

## Project

To illustrate a prototype usage case we are going to develop a program that can register geometrical forms in a cartesian plan. Each geometrical form have a list of points and only this. Instead of sub-classing GeometricalForm to create Squares, Circles, Rectangles and Triangles we are going to create a registry of common used geometrical forms, and every time a client code needs one of these common forms we can only clone the pre-initialized object.

First of all let's create the GeometricalForm class:

geometrical_form.py

```python
class GeometricalForm(Prototype):
    def __init__(self):
        self.points = []
```

Now let's create a a Prototype interface and implement it on GeometricalForm:

prototype.py

```python
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
```

geometrical_form.py

```python
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
```

Note that it's possible to pass a clone object to the constructor, this way the constructor can clone the object by it-self. Inside the clone function we just need to call the class constructor using *self* as parameter. Now let's crete a registry using a dictionary as a hashmap, to register common geometrical forms:

geometrical_forms_registry.py

```python
from geometrical_form import GeometricalForm
from point import Point

class GeometricalFormsRegistry:
    def __init__(self):
        self.common_forms = {}
        self.populate_common_forms()

    def populate_common_forms(self):
        # register square
        self.common_forms['square'] = GeometricalForm(points=[
            Point(0, 0),
            Point(0, 1),
            Point(1, 1),
            Point(1, 0),
        ])

        # register rectangle
        self.common_forms['rectangle'] = GeometricalForm(points=[
            Point(0, 0),
            Point(0, 2),
            Point(2, 1),
            Point(1, 0),
        ])

        # register triangle
        self.common_forms['triangle'] = GeometricalForm(points=[
            Point(0, 0),
            Point(0, 1),
            Point(1, 0),
        ])

    def get(self, form_name: str) -> GeometricalForm:
        return self.common_forms.get(form_name)
```

Now let's create a client code to use the all the code we created:

main.py

```python
from geometrical_forms_registry import GeometricalFormsRegistry

if __name__ == '__main__':
    registry = GeometricalFormsRegistry()

    # square
    print('give me a square')
    square = registry.get('square')
    print(str(square))
    print("")

    # rectangle
    print('give me a rectangle')
    rectangle = registry.get('rectangle')
    print(str(rectangle))
    print("")

    # triangle
    print('give me a triangle')
    triangle = registry.get('triangle')
    print(triangle)
    print("")
```

Thanks for reading :) feel free to fork this project and increment it.
