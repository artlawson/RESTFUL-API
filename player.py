#player.py

class Player():
    def __init__(self, team_id,
    name, number, weight, position, experience, games = None):
        # don't pass it an id, an id should be created with player automatically
        self.id = id(self)
        self.team_id = team_id
        self.number = number 
        self.name = name
        self.weight = weight
        self.position = position
        self.experience = experience
        self.games = games

        #if self.experience != "Rookie":
         #   self.experience = int(self.experience)

    def falsify(self):
        return {"id" : self.id, "name" : self.name, "team id" : self.team_id, "weight" : self.weight, 
    "experience": self.experience, "games" : self.games, "number" : self.number} 

    def shorten(self):
        return {"id": self.id, "name": self.name}

    







#potentially super class and let 
#dict with id : player object,      call on id, then id and get player object