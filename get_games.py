import flask
import requests
import json
import random
import datetime,os
import path
import time
import  re

def fetchingData():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = []
    for games in response['games']:
        game_details.append(games)
    return game_details

# category=[]
# for i in (fetchingData()):
#     if (i['categories']['en']) not in category and re.search('Featured'.lower(),str(i['categories']['en']).lower()) :
#         category.append((i['categories']['en']))
# for i in category:
#     print(i)
# print(fetchingData())
category = ['Arcade','Puzzle & Logic','Sports & Racing','Strategy','Adventure','Action','Featured']


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
# update_game_data()
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

    print("Sending 5 games",game_details)
    return game_details


def single_game():
    response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
    game_details = response['games'][random.randint(0,50)]
    return game_details



def get_game_by_keyword(keywords):
    matches=[]
    with open('games_2020-11-16.json','r') as games:
        # print(len(json.load(games)['games']))
        game_keywords = ['car', 'football', 'cricket', 'chess', 'building', 'criss', 'cross', 'criss-cross', 'card', 'board',
                    'hunt', 'treasure', 'memory', 'brain', 'checkers', 'bubble', 'bubbles', 'box', 'pokemon', 'test', 't',
                    'twenty','t-twenty', 't-20', 'space', 'sack','defence', 'military', 'fighter', 'fighting', 'fight',
                    'combat', 'kombat', 'war', 'racing', 'bike','bus', 'shoot', 'shooting','shotting','shoting', 'fireballs','fireball', 'ball'
                    ,'bowl' ,'race', 'racing', 'missiles', 'missile', 'classic', 'aim', 'aiming', 'gravity','hard']
        sentence_fillers=['me','i','get','find','show','you','am','are','some']
        keywords_list=list(map(str,(keywords).split()))

        print(keywords_list)
        loop=1
        final_list=[]
        for k in keywords_list:
            print("Loop count = ", loop, " for -> ",k)
            if not (k in sentence_fillers or k not in game_keywords):
                print("removed -> ",k)
                final_list.append(k)
                loop += 1

        keywords_list=final_list
        print("keywords searching ->", keywords_list)

        for a in (json.load(games)['games']):
            for keyword in keywords_list:
                if  re.search(keyword.lower(),str(a['description']['en']).lower())  or \
                        re.search(keyword.lower() , str(a['name']['en']).lower()) or \
                        re.search(keyword.lower() , str(a['tags']['en']).lower()) or \
                        re.search(keyword.lower(),str(a['categories']['en']).lower()):
                    matches.append(a)
    return matches



# print(len(get_game_by_keyword('cricket games ')))
# print(re.search("cricket games ".lower()," hi , wanna play some cricket".lower()))
def get_five_games_by_keyword(keyword):
    matches=[]

    with open('games_2020-11-16.json','r') as games:
        # print(len(json.load(games)['games']))
        while len(matches)<5:
            for a in json.load(games)['games']:
                for keywords in list(keyword):
                    # for a in (json.load(games)['games']):
                    #     print(a)
                    if  re.search(keywords.lower(),str(a['description']['en']).lower())  or \
                 re.search(keywords.lower() , str(a['name']['en']).lower()) or \
                 re.search(keywords.lower() , str(a['tags']['en']).lower()) or \
                 re.search(keywords.lower(),str(a['categories']['en']).lower()):
                        matches.append(a)
        # while len(matches)<5:
        #     for keywords  in list(keyword):
        #         for a in (json.load(games)['games']):
        #             print(a)
                    # if  re.search(keywords.lower(),str(a['description']['en']).lower())  or \
                    #      re.search(keywords.lower() , str(a['name']['en']).lower()) or \
                    #      re.search(keywords.lower() , str(a['tags']['en']).lower()) or \
                    #      re.search(keywords.lower(),str(a['categories']['en']).lower()):
                    #     matches.append(a)

                # print(a['name']['en'],a['description']['en'], a['url'])
            # print(a)
    # print(len(matches))
    return matches


def pc_or_mobile_game(mobile=False):

    with open('games_2020-11-16.json', 'r') as games:
        # print(len(json.load(games)['games']))
        count=0
        game = []
        for a in (json.load(games)['games']):

            if(mobile) :
                if a['isPortrait']:
                    # pass
                    count+=1
                    game.append(a)

            else:
                if not a['isPortrait']:
                    count += 1
                    game.append(a)
    return  game


def games_by_category(category):

    matches = []
    if(category==None):
        response = (requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en")).json()
        return response['games'][0:random.randint(0,len(response['games'])-1)]
        # print("No game available of this category")
        # return None
    print("Category :- ",category)
    with open('games_2020-11-16.json', 'r') as games:
        for a in (json.load(games)['games']):
            if re.search(category.lower(), str(a['categories']['en']).lower()):
                matches.append(a)

                # print(a['name']['en'],a['description']['en'], a['url'])
            # print(a)

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

    """print("----------------------------Sending games :-----------------------------")
    for i in games:
        print(i)
    print("----------------------------Sending games :-----------------------------")"""
    return games
# print(games_by_category("strategy"))
category = ['arcade','puzzle','logic','sports','racing','strategy','adventure','action','featured']


def is_category(category,reply_text):
    print(category,reply_text)

    if len(reply_text)==0:
        return None
    for cat in category:
        print("CAT ->", cat, " reply ->", str(list(reply_text)[0]).lower())
        if re.search(cat.lower(),str(list(reply_text)[0]).lower()):
            return  cat
    print("None found !")
    return None



# print(is_category(category,{['action']}))
# from reply_methods import  five_game_payload
# user_id="18BCS6714"
# input_text="action"
# payload=five_game_payload(user_id,games_by_category(is_category(category,input_text)))
# print(payload)


# print(get_five_games_by_keyword("Get me cricket games"))
# print(pc_or_mobile_game(mobile=False))
# print(len(get_games_by_keyword('racing')))


#  Utility method :
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



