class Vehicle:
    def __init__(self, type, model, price):
        self.type, self.model, self.price, self.owner = type, model, price, None

    def buy(self, money, owner):
        if self.price > money:
            return "Sorry, not enough money"
        if self.owner:
            return "Car already sold"
        self.owner = owner
        return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"

    def sell(self):
        if self.owner:
            self.owner = None
        return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"
