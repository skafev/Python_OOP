from PythonOOP.project_pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemon:
            if pokemon_name == p.name:
                self.pokemon.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            res += f"- {p.pokemon_details()}\n"
        return res


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
