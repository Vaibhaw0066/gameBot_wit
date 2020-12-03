import flask
import requests
import json
import random
import datetime,os
import path
import time

def fetchingData():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = []
    for games in response['games']:
        game_details.append(games)
    return game_details

# print(fetchingData())


def update_game_data():
    date = datetime.datetime.today().date()
    file_name='games_'+str(date)+'.json'
    if(file_name not in os.listdir()):
        response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
        game_details = {}
        games=response
    # print(response)
        with open(file_name,'w') as outfile:
            json.dump(games,outfile)

        # delete_older_data()

# with open('games_2020-10-22.json','r') as games:
#     for a in (json.load(games)['games']):
#         print(a['name']['en'])


def top_5_games():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = []
    i=0
    while(i<5):
        game_details.append(response['games'][random.randint(0,240)])
        i+=1
    return game_details

def single_game():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = response['games'][random.randint(0,50)]
    return game_details

