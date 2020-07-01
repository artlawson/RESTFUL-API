#team.py

class Team():
    def __init__(self,conference_id, name,
        city, founding_year, championships):
        self.id = id(self)
        self.name = name
        self.city = city
        self.conference_id = conference_id
        self.founding_year = founding_year
        self.championships = championships
        self.roster = {}

    def falsify(self):
        return {"name": self.name, "id" : self.id,"Conference" : self.conference_id, "City": self.city,  "roster" : self.roster, 
        "founding year" : self.founding_year, "Number of Championships" : self.championships}

    def build_roster(self, player_list):
        self.roster.clear()
        pre_roster = [i for i,j in player_list.items() if j == self.id]

        for player in pre_roster:
            p_id = player[0]
            p_name = player[1]
            self.roster[p_name] = p_id
        return self.roster
    def shorten(self):
        return  {"id": self.id, "name": self.name}
     

