# Prototype

This project implements a use case for a Design Pattern, the Prototype. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/prototype).

## What it is?

Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

## Project

To illustrate a prototype usage case we are going to develop a program that can register geometrical forms in a cartesian plan. Each geometrical form have a list of points and just this. Instead of subclassing GeometricalForm to create Squares, Circles, Rectangles and Triangles we are going to create a registry of common used geometrical forms, and every time a client code needs one of these common forms we can only clone the pre-initialized object.

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

```

geometrical_form.py

```python

```

Now let's crete a registry using a dictionary as a hashmap, to register common geometrical forms:

geometrical_forms_registry.py

```python

```

Now let's create a client code to use the all the code we created:

main.py

```python

```

Thanks for reading :) feel free to fork this project and increment it.
