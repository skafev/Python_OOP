class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > 0:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                self.__animal_capacity -= 1
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker_to_fire = [w for w in self.workers if w.name == worker_name]
        if worker_to_fire:
            worker = worker_to_fire[0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries = 0
        for worker in self.workers:
            all_salaries += worker.salary
        if all_salaries > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        budget_left = self.__budget - all_salaries
        self.__budget = budget_left
        return f"You payed your workers. They are happy. Budget left: {budget_left}"

    def tend_animals(self):
        all_cost = 0
        for animal in self.animals:
            all_cost += animal.get_needs()
        if all_cost > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        budget_left = self.__budget - all_cost
        self.__budget = budget_left
        return f"You tended all the animals. They are happy. Budget left: {budget_left}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals"
        lions = 0
        result_lions = []
        tigers = 0
        result_tigers = []
        cheetahs = 0
        result_cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions += 1
                result_lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers += 1
                result_tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs += 1
                result_cheetahs.append(animal)
        result += f"\n----- {lions} Lions:\n"
        if result_lions:
            result += '\n'.join(map(str, result_lions))
        result += f"\n----- {tigers} Tigers:\n"
        if result_tigers:
            result += '\n'.join(map(str, result_tigers))
        result += f"\n----- {cheetahs} Cheetahs:\n"
        if result_cheetahs:
            result += '\n'.join(map(str, result_cheetahs))
        return result

    def workers_status(self):
        result = ""
        result += f"You have {len(self.workers)} workers"
        keepers = 0
        result_keepers = []
        caretakers = 0
        result_caretakers = []
        vets = 0
        result_vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers += 1
                result_keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers += 1
                result_caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets += 1
                result_vets.append(worker)
        result += f"\n----- {keepers} Keepers:\n"
        if result_keepers:
            result += '\n'.join(map(str, result_keepers))
        result += f"\n----- {caretakers} Caretakers:\n"
        if result_caretakers:
            result += '\n'.join(map(str, result_caretakers))
        result += f"\n----- {vets} Vets:\n"
        if result_vets:
            result += '\n'.join(map(str, result_vets))
        return result
