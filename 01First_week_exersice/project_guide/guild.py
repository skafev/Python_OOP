class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild != "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        filtered_player = [p for p in self.list_of_players if p == player]
        if filtered_player:
            return f"Player {player.name} is already in the guild."
        self.list_of_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        filtered_player = [p for p in self.list_of_players if p.name == player_name]
        if not filtered_player:
            return f"Player {player_name} is not in the guild."
        player = filtered_player[0]
        self.list_of_players.remove(player)
        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        res = f"Guild: {self.name}\n"
        for p in self.list_of_players:
            res += p.player_info()
        return res


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
