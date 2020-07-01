#league.py

class League():
    def __init__(self, name, conferences):
        self.name = name
        self.conferences = conferences
        self.all_players = {} # str name to object
        self.all_teams = {}
        

    def con_falsify(self):
        #figure out what we would want to return in this
        temp = list(self.conferences.values())
        output = {}
        for obj in temp:
            output[obj.id] = obj.name

        return {"League Name" : self.name, "Conferences" : output}

    def players_falsify(self):
        #figure out what we would want to return in this
        temp = list(self.all_players.values())
        output = {}
        for obj in temp:
            output[obj.id] = obj.name

        return {"League Name" : self.name, "Players" : output}

    def teams_falsify(self):
        #figure out what we would want to return in this
        temp = list(self.all_teams.values())
        output = {}
        for obj in temp:
            output[obj.id] = obj.name

        return {"League Name" : self.name, "Teams" : output}


    