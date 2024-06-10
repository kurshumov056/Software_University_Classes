class Player:

    #skills contains skill:mana cost
    skills = {}
    guild = "Unaffiliated"


    def __init__(self, player_name: str, hp: int, mp: int):
        self.player_name = player_name
        self.hp = hp
        self.mp = mp


    def add_skill(self, skill_name: str, skill_cost: int):
        if skill_name not in self.skills.keys():
            self.skills.update({skill_name:skill_cost})
            return f"Skill {skill_name} added to the collection of the player {self.player_name}"
        else:
            return f"Skill already added"

    def player_info(self):
        return f"Name: {self.player_name} \nGuild: {self.guild} \nHP: {self.hp} \nMP: {self.mp} \n{self.skills}\n"
    



