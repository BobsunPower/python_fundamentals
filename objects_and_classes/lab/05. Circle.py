class Circle:
    def __init__(self, dia):
        self.dia, self.rad = dia, dia / 2

    def calculate_circumference(self):
        return 3.14 * self.dia

    def calculate_area(self):
        return 3.14 * self.rad ** 2

    def calculate_area_of_sector(self, ngl):
        return (ngl / 360) * self.calculate_area()
