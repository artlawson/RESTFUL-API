from player import *
from team import *
from conference import *
from league import *

#examples

#conferences
West = Conference( "West", { "T1" : "Mavericks", "T2": "Lakers", "T3" : "Warriors"})
East = Conference( "East", { "T1" : "Hawks", "T2": "Heat", "T3" : "Celtics"})

#team
Lakers = Team(West.id, "Lakers", "Los Angeles", 1947, 17)

#players
Robbie = Player(Lakers.id, "Robbie", 1, 190,  "PG",  12, {"Clippers" : "W", "Heat": "L", "Knicks": "W" })
Boo = Player(Lakers.id, "Boo",2, 215, "SG",12, {"Clippers" : "W", "Heat": "L", "Knicks": "W" })
Caleb = Player(Lakers.id, "Caleb",5, 200, "SF", 12, {"Clippers" : "W", "Heat": "L", "Knicks": "W" })
#team
free_agency = Team(0, "Free Agency", "n/a", 0000, 318)

#league
NBA = League("NBA", {West.id: West, East.id: East})

#helper function
def roast(player):
    return (player.id, player.name)

#lists to summon from
NBA.all_players = {Boo.id : Boo, Robbie.id : Robbie, Caleb.id : Caleb}
playerz = {roast(Boo) : Boo.team_id, roast(Robbie) : Robbie.team_id, roast(Caleb): Caleb.team_id} #roast has id, team id
Lakers.build_roster(playerz)
NBA.all_teams = {Lakers.id : Lakers}



#stored players 

'''

def fresh_player(play_name,
 play_team_id, weight, play_position, play_team, play_experience):
    if play_experience != "Rookie":
        play_experience = int(play_experience)
    new = Player()
    setattr(Player, name, play_name)
    setattr(player, team_id, int(play_team_id))
    setattr(Player, weight, int(play_weight))
    setattr(Player, position, play_position)
    setattr(Player, team, play_team)
    setattr(Player, experience, play_experience)
    return new
'''

