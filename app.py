#app.py

#open folder, then type flask run

from flask import Flask, request, jsonify
from examples import *
#from flask_sqlalchemy import SQLAlchemy
import json
import random

#set up file structure correctly so things can be imported
app = Flask(__name__)
#db = SQLAlchemy(app)


print(Robbie.id, "Rob")
print(Lakers.id, "Lakers")

@app.route('/v1/League/Players', methods = ['GET'])
def all_players():
    return NBA.players_falsify()

  
@app.route('/v1/League/Players/<p_id>', methods = ['GET'])
def get_player(p_id):
    p_id = int(p_id)
    if NBA.all_players.get(p_id, None):
        return NBA.all_players[p_id].falsify()
    print("something is wrong")
    return "There is no valid Player with id '" + str(p_id) + "'."

@app.route('/v1/League/Players/<p_id>', methods = ['PATCH'])

def edit_player(p_id):
    p_id = int(p_id)
    output = request.get_json() #returns valid python dictionary (if input was string, it would return string)
    if not NBA.all_players.get(p_id, None):
        return "There is no valid Player with id '" + str(p_id) + "'."
    player = NBA.all_players[p_id]

    if output.get("name", None):
        name = output["name"]
        if player.name != name:
            player.name = name
    if output.get("position",None):
        position = output["position"]
        if player.position != position:
            player.position = position
    if output.get("number", None):
        number = output["number"]
        if player.number != number:
            player.number = number
    if output.get("team_id", None):
        team_id = output["team_id"]
        if player.team_id != team_id:
            player.team_id = team_id
    if output.get("weight",None):
        weight = output["weight"]
        if player.weight != weight:
            player.weight = weight
    if output.get("experience", None):
        experience = output["experience"]
        if player.experience != experience:
            player.experience = experience
    if output.get("games",None):
        games = output["games"]
        if player.games != games:
            player.games = games

    return player.falsify()

@app.route('/v1/League/Players/<p_id>', methods = ['DELETE'])   #######FIX THE ROUTES

def delete_player(p_id):
    p_id = int(request.get_json())
    if not NBA.all_players.get(p_id, None):
        return "There is no valid Player with id '" + str(p_id) + "'."
    player = NBA.all_players[p_id]
    former_team = NBA.all_teams[player.team_id]
    del player
    #former_team.build_roster()
    #return former_team.falsify()               
    return "Player deleted successfully!"



@app.route('/v1//League/Players/new', methods = ['POST'])

def new_player():
    #converts cont dictionary into valid player
    output = request.get_json() #returns valid python dictionary (if input was string, it would return string)
    name = output["name"]
    team_id = output["team_id"]
    weight = output["weight"]
    position = output["position"]
    experience = output["experience"]
    number = output["number"]
    games = output["games"]
    globals()[name] = Player(Lakers.id, name, number, weight, position, experience, games) #converts string to variable name 
    new_player = globals()[name]
    NBA.all_players[new_player.name] = new_player
    return "New player has been added successfully!"
    ###
    #return new_player.falsify()
    #tests that new player is actually created
    #####


    #try:
     #   make_response()

@app.route('/v1/League/Teams',  methods = ['GET'])

def all_teams():
    return NBA.teams_falsify()

@app.route('/v1/League/Teams/<tm_id>',  methods = ['GET'])

def get_team(tm_id):
    #idd = int(tm_id[1:-1])
    idd = int(tm_id)
    if NBA.all_teams.get(idd, None):
        return NBA.all_teams[idd].falsify()
    return "There is no team with id '" + str(idd) + "'."

@app.route('/v1/League/Teams/<tm_id>',  methods = ['PATCH'])

def edit_team(tm_id):
    tm_id = int(tm_id[1:-1])
    output = request.get_json() #returns valid python dictionary (if input was string, it would return string)
   
    if not NBA.all_teams.get(tm_id, None):
        return "There is no valid Team with id '" + str(tm_id) + "'."
    team = NBA.all_teams[tm_id]

    if output.get("name", None):
        name = output["name"]
        if team.name != name:
            team.name = name
    if output.get("city",None):
        city = output["city"]
        if team.city != city:
            team.city = city
    if output.get("championships", None):
        championships = output["championships"]
        if team.championships != championships:
            teamp.championships = championships
    if output.get("founding_year", None):
        founding_year = output["founding_year"]
        if team.founding_year != founding_year:
            team.founding_year = founding_year

    if output.get("roster", None):
        roster = output["roster"]
        if team.roster != roster:
            team.roster = roster

    return team.falsify()

@app.route('/v1/League/Teams/',  methods = ['DELETE'])

def delete_team():
    tm_id = int(request.get_json()) #returns valid python dictionary (if input was string, it would return string)
    if not NBA.all_teams.get(tm_id, None):
        return "There is no valid Team with id '" + str(tm_id) + "'."
    team = NBA.all_teams[tm_id]
    for player in list(NBA.all_players.values()):
        if player.team_id ==tm_id:
            player.team_id = free_agency.id
    del team
    return "Team deleted successfully!"



@app.route('/v1/League/Teams/new', methods = ['POST'])  #fix the routes!!!

def new_team():
    output = request.get_json() #returns valid python dictionary (if input was string, it would return string)
    conference_id = globals()[output["conference"]].id
    name = output["name"]
    founding_year = output["founding year"]
    championships = output["championships"]
    city = output["city"]
    globals()[name] = Team(conference_id, name, city, founding_year, championships) #converts string to variable name 
    globals()[output["conference"]].team_list[globals()[name].id] = globals()[name]
    add_team = globals()[name]
    return add_team.falsify()
    


@app.route('/v1/League/Conferences/<idd>', methods = ['GET'])

def get_conference(idd):
    idd = int(idd)
    if NBA.conferences.get(idd, None):
        return NBA.conferences[idd].falsify()
    return "There is no conference with id '" + str(idd) + "'."

@app.route('/v1/League/Conferences', methods = ['GET'])

def conferences():
    return NBA.con_falsify()

#helper link
#https://www.google.com/search?q=make+a+website+from+flask+api&oq=make+a+website+from+flask+api&aqs=chrome..69i57j33l4.7583j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_MTOAXqHTCovl-gSEi7jIBA28
