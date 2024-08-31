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
    