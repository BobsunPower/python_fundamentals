class Storage:
    def __init__(self, capacity):
        self.capacity, self.storage = capacity, []

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage
