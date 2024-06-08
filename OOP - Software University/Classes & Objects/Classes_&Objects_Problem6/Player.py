



class Player:

    #skills contains skill:mana cost
    self.skills = dict()
    self.guild = "Unaffiliated"


    def __init__(self, player_name: str, hp: int, mp: int):
        self.player_name = name
        self.hp = hp
        self.mp = mp


    def add_skill(self, skill_name: str, skill_cost: int):
        if skill_name not in self.skills.keys():
            self.skills.update({skill_name:skill_cost})
            return f"Skill {skill_name} added to the collection of the player {player_name}"
        else:
            return f"Skill already added"

    def player_info(self):
        return f"Name: {player_name} \nGuild: {guild_name} \nHP: {hp} \nMP: {mp}}"
    



