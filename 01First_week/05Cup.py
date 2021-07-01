class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.amount_of_water = 0
        self.total = self.size - self.quantity

    def fill(self, n):
        if self.total >= n:
            self.amount_of_water += n
            self.quantity += n
            self.total -= self.amount_of_water

    def status(self):
        return self.total


cup = Cup(10, 5)
cup.fill(3)
print(cup.status())
