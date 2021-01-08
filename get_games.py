
import requests
import json
import random
import datetime,os
import  re


""" =========================================  Methods to fetch games  ========================================"""
# Fetching game data from Gamezop API
def fetchingData():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = []
    for games in response['games']:
        game_details.append(games)
    return game_details

category = ['Arcade','Puzzle & Logic','Sports & Racing','Strategy','Adventure','Action','Featured']

#  Updating game data from game GameZop API
def update_game_data():
    date = datetime.datetime.today().date()
    file_name='games_'+str(date)+'.json'
    if(file_name not in os.listdir()):
        response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
        game_details = {}
        games=response
        with open(file_name,'w') as outfile:
            json.dump(games,outfile)

#  Returning random 5 games in a list
def top_5_games():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = []
    i=0
    while(i<5):
        game_details.append(response['games'][random.randint(0,240)])
        i+=1

    return game_details

#  Returns single game in JSON format
def single_game():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = response['games'][random.randint(0,50)]
    return game_details


# Returns all the games matching the keywords given by user
def get_game_by_keyword(keywords):
    matches=[]
    keywords=keywords.lower()

    with open('Assets/games_2021-01-08.json','r') as games:

        # increase the game keyword list to improve the game matching rates
        game_keywords = ['car', 'football', 'cricket', 'chess', 'building', 'criss', 'cross', 'criss-cross', 'card', 'board',
                    'hunt', 'treasure', 'memory', 'brain', 'checkers', 'bubble', 'bubbles', 'box', 'pokemon', 'test', 't',
                    'twenty','t-twenty', 't-20', 'space', 'sack','defence', 'military', 'fighter', 'fighting', 'fight',
                    'combat', 'kombat', 'war', 'racing', 'bike','bus', 'shoot', 'shooting','shotting','shoting', 'fireballs',
                    'fireball', 'ball','bowl' ,'race', 'racing', 'missiles', 'missile', 'classic', 'aim', 'aiming', 'gravity',
                    'hard','insane','cat','dog','pet','fly','plane']
        sentence_fillers=['me','i','get','find','show','you','am','are','some']
        keywords_list=list(map(str,(keywords).split()))
        loop=1
        final_list=[]
        for k in keywords_list:
            if not (k in sentence_fillers or k not in game_keywords):
                final_list.append(k)
                loop += 1

        keywords_list=final_list

        for a in (json.load(games)['games']):
            for keyword in keywords_list:
                if  re.search(keyword.lower(),str(a['description']['en']).lower())  or \
                        re.search(keyword.lower() , str(a['name']['en']).lower()) or \
                        re.search(keyword.lower() , str(a['tags']['en']).lower()) or \
                        re.search(keyword.lower(),str(a['categories']['en']).lower()):
                    matches.append(a)
    return matches


# Getting 5 games of particular category
def games_by_category(category):

    matches = []
    if(category==None):
        response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
        return response['games'][0:random.randint(0,len(response['games'])-1)]
    print(f' Fetching games of {category} category')
    with open('Assets/games_2021-01-08.json', 'r') as games:
        for a in (json.load(games)['games']):
            if re.search(category.lower(), str(a['categories']['en']).lower()):
                matches.append(a)
    games=[]
    count=0
    while True:
        g= matches[random.randint(0,len(matches)-1)]
        if count==5:
            break
        if g not in games:
            games.append(g)
        count+=1

    while len(games)<5:
        g = matches[random.randint(0, len(matches) - 1)]
        if g not in games:
            games.append(g)
    return games

category = ['arcade','puzzle','logic','sports','racing','strategy','adventure','action','featured']

# Matching if given category exists or not
def is_category(category,reply_text):
    print(category,reply_text)

    if len(reply_text)==0:
        return None
    for cat in category:
        if re.search(cat.lower(),str(list(reply_text)[0]).lower()):
            return  cat
    print("None found !")
    return None




# Getting 5  games by keyor[Beta]
"""
def get_five_games_by_keyword(keyword):
    matches=[]

    with open('Assets/games_2021-01-08.json','r') as games:
        while len(matches)<5:
            for a in json.load(games)['games']:
                for keywords in list(keyword):
                    if  re.search(keywords.lower(),str(a['description']['en']).lower())  or \
                 re.search(keywords.lower() , str(a['name']['en']).lower()) or \
                 re.search(keywords.lower() , str(a['tags']['en']).lower()) or \
                 re.search(keywords.lower(),str(a['categories']['en']).lower()):
                        matches.append(a)
    return matches
"""

# Returns games compatible to PC or small resolution device [Beta]
"""
def pc_or_mobile_game(mobile=False):

    with open('Assets/games_2021-01-08.json', 'r') as games:
        count=0
        game = []
        for a in (json.load(games)['games']):

            if(mobile) :
                if a['isPortrait']:
                    count+=1
                    game.append(a)

            else:
                if not a['isPortrait']:
                    count += 1
                    game.append(a)
    return  game
"""




#  ================================================   Utility methods    ===============================================


""" Rounding of the total gamePlays to nearest thousands, millions or billion  """
def get_figures(num):
    num=float(num)
    x=num/1000000000
    if(x>=1):
        # print(round(x,2),' billion')
        return str(round(x,2))+'B'

    x=num/1000000
    if(x>=1):
        # print(round(x,2), 'million')

        return str(round(x,2))+'M'

    x=num/1000
    if(x>=1):
        return str(round(x,2)) + 'k'

    return str(num)


