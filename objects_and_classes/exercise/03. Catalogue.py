class Catalogue:
    def __init__(self, name):
        self.name, self.products = name, []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [i for i in self.products if i.startswith(first_letter)]

    def __repr__(self):
        items = "\n".join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{items}"
