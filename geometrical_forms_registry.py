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