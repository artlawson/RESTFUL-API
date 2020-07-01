#conference.py

class Conference():
    #need to add similar to buold roster method for teams
    #think about moving cities to team object to account for ^
    def __init__(self, name, team_list):
        self.id = id(self)
        self.name = name
        self.team_list = team_list

        

    def falsify(self):
        return {"id" : self.id, "name": self.name, "team list" : self.team_list} 



