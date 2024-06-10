
from Guild_System.Player import Player



class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = list()
        
    
    def assign_player(self, player: Player):
        self.player = player
        
        if player.guild == 'Unaffiliated':
            player.guild == self.name
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.player_name} to the guild {self.name}"
            
        if player.player_name in self.players:
            return f"Player {player.player_name} is already in the guild"


        if player.guild != 'Unaffiliated' and player.guild not in Guild:
            return f"Player {player.player_name} is in another guild."

    def guild_info(self):
        result = f"Guild: {self.name}"
        for player in self.players:
            result += "\n" + player.player_info()
        return result
    def kick_player(self, player_name: str):
        for player in self.players:
            if player.player_name == player_name:
                player.guild ='Unaffiliated'

                return f"Player {player_name} has been removed from guild"

        else:
            return "Player isn't in any of the existing guilds"



 
