class Inventory:
    def __init__(self, capacity):
        self.__capacity, self.items = capacity, []

    def add_item(self, item):
        return self.items.append(item) if len(self.items) < self.__capacity else "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"


# •	add_item(item) - adds the item in the inventory if there is space for it. Otherwise, returns
# "not enough room in the inventory"
# •	get_capacity() - returns the value of __capacity
# •	__repr__() - returns "Items: {items}.\nCapacity left: {left_capacity}". The items should be separated by ", "
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
