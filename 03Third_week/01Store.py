class Store:
    items = {}

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity

    def __repr__(self):
        return str(f"{self.name} of type {self.type} with capacity {self.capacity}")

    @staticmethod
    def can_remove_item(items, item_name, amount):
        return item_name in items \
               and amount <= items[item_name]

    @classmethod
    def from_size(cls, name, type, size: int):
        new_capacity = round(size * 0.5)
        return cls(name, type, new_capacity)

    def add_item(self, item_name):
        if len(Store.items) > self.capacity:
            return "Not enough capacity in the store"
        Store.items[item_name] = 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if not self.can_remove_item(self.items, item_name, amount):
            return f"Cannot remove {amount} {item_name}"
        Store.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
