class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        self.__dough = dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, toppings):
        self.__toppings[toppings] = toppings.weight

    def add_topping(self, topping):
        if self.__toppings_capacity == 0:
            raise ValueError("Not enough space for another topping")
        elif topping.topping_type not in self.__toppings:
            self.__toppings[topping.topping_type] = topping.weight
        elif topping.topping_type in self.__toppings:
            self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total = self.__dough.weight + sum(self.__toppings.values())
        return total

