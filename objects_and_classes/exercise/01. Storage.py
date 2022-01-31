class Storage:
    def __init__(self, capacity):
        self.capacity, self.storage = capacity, []

    def add_product(self, product):
        len(self.storage) < self.capacity and self.storage.append(product)

    def get_products(self):
        return self.storage
