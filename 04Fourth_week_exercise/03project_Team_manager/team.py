class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players):
        self.__players = players

    def add_player(self, player):
        player_to_add = [p for p in self.__players if p == player]
        if not player_to_add:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name):
        player_to_remove = [p for p in self.__players if p.name == player_name]
        if not player_to_remove:
            return f"Player {player_name} not found"
        p_to_remove = player_to_remove[0]
        self.__players.remove(p_to_remove)
        return p_to_remove
