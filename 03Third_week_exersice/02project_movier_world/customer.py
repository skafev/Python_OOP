class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []
        self.rented_dvds_names = []

    def __repr__(self):
        return str(f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's "
                   f"({', '.join(map(str, self.rented_dvds_names))})")
