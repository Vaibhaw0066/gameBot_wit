
def text_message_payload(user_id,message):
    text_messsage={"users":   [user_id],
               "message": {"text": message},
               }
    return text_messsage


def quick_reply_payload(user_id,title):
    reply = {"users": [user_id], "message": {"quick_replies":
                                            [
                                                {"content_type": "text",
                                                 "title": title,
                                                 "payload": title
                                                 }
                                            ]
                                            }
                        }
    return reply

def msg_with_quick_reply_payload(user_id,msg,title1,title2):
    reply = {"users": [user_id], "message": { "text":msg,
                                            "quick_replies":
                                            [
                                                {"content_type": "text",
                                                 "title": title1,
                                                 "payload": title1
                                                 },

                                                {"content_type": "text",
                                                 "title": title2,
                                                 "payload": title2
                                                 }

                                            ]
                                            }
                        }
    return reply




def linked_button_payload(user_id,title,link):

    button_with_link= { "users":[user_id], "message":{ "attachment":
                                                     { "type":"template",
                                                       "payload":{ "template_type": "button", "text": "Hi, I am a good bot...!",
                                                                   "buttons": [{ "title": title, "type": "web_url", "url": link }]
                                                                 }
                                                       }
                                                 }
                  }
    return  button_with_link


def msg_with_quick_reply_and_GIF_payload(user_id,msg,title1,title2,GIF):
    reply = {"users": [user_id], "message": { "text":msg,
                                            "quick_replies":
                                            [
                                                {"content_type": "text",
                                                 "title": title1,
                                                 "payload": "category"
                                                 },

                                                {"content_type": "text",
                                                 "title": title2,
                                                 "payload": title2
                                                 }

                                            ],
                                              "attachment": {"type": "template",
                                                             "payload": {"template_type": "generic",
                                                                         "elements": [{"image_url": GIF}]
                                                                         }
                                                             },
                                            }
                        }
    return reply

# https://media.giphy.com/media/QYkX9IMHthYn0Y3pcG/giphy.gif

def five_game_payload(user_id,game_obj_list):

    print()
    # print(game_obj_list)
    print()

    card = pack={ "users":[user_id],
               "message": { "attachment":{ "type":"template",
                                      "payload":{ "template_type":"generic",
                                                  "elements":[ { "title": game_obj_list[0]['name']['en'],
                                                                 "subtitle":"",
                                                                  "image_url":game_obj_list[0]['assets']['cover'] ,
                                                                   "buttons": [
                                                                               { "title": "Preview", "type": "web_url", "url": str(game_obj_list[0]['gamePreviews']['en'])},
                                                                               { "title": "Play", "type": "web_url", "url": game_obj_list[0]['url'] }
                                                                               ]
                                                                },
                                                               {"title": game_obj_list[1]['name']['en'],
                                                                "subtitle": "",
                                                                "image_url": game_obj_list[1]['assets']['cover'],
                                                                "buttons": [
                                                                    {"title": "Preview", "type": "web_url", "url": str(
                                                                        game_obj_list[1]['gamePreviews']['en'])},
                                                                    {"title": "Play", "type": "web_url",
                                                                     "url": game_obj_list[1]['url']}
                                                                ]
                                                                },
                                                               {"title": game_obj_list[2]['name']['en'],
                                                                "subtitle": "",
                                                                "image_url": game_obj_list[2]['assets']['cover'],
                                                                "buttons": [
                                                                    {"title": "Preview", "type": "web_url", "url": str(
                                                                        game_obj_list[2]['gamePreviews']['en'])},
                                                                    {"title": "Play", "type": "web_url",
                                                                     "url": game_obj_list[2]['url']}
                                                                ]
                                                                },
                                                               {"title": game_obj_list[3]['name']['en'],
                                                                "subtitle": "",
                                                                "image_url": game_obj_list[3]['assets']['cover'],
                                                                "buttons": [
                                                                    {"title": "Preview", "type": "web_url", "url": str(
                                                                        game_obj_list[3]['gamePreviews']['en'])},
                                                                    {"title": "Play", "type": "web_url",
                                                                     "url": game_obj_list[3]['url']}
                                                                ]
                                                                },
                                                               {"title": game_obj_list[4]['name']['en'],
                                                                "subtitle": "",
                                                                "image_url": game_obj_list[4]['assets']['cover'],
                                                                "buttons": [
                                                                    {"title": "Preview", "type": "web_url", "url": str(
                                                                        game_obj_list[4]['gamePreviews']['en'])},
                                                                    {"title": "Play", "type": "web_url",
                                                                     "url": game_obj_list[4]['url']}
                                                                ]
                                                                }

                                                             ]
                                                  }
                                      }
                       }
           }

    return  card


# 'Game Plays :'+ str(game_obj_list[0]['gamePlays']   -> gameplays


def single_game_payload(user_id,game):

    print("Game -> ",game)
    pack={ "users":[user_id],
           "message":{ "attachment":{ "type":"template",
                                      "payload":{ "template_type":"generic",
                                                  "elements":[ { "title": game['name']['en'],
                                                                 "subtitle":"",
                                                                  "image_url":game['assets']['cover'] ,
                                                                   "buttons": [
                                                                               { "title": "Preview", "type": "web_url", "url": str(game['gamePreviews']['en'])},
                                                                               { "title": "Play", "type": "web_url", "url": game['url'] }
                                                                               ]
                                                                }

                                                             ]
                                                  }
                                      },
                       "quick_replies":
                           [
                               {"content_type": "text",
                                "title": "more",
                                "payload": "more"
                                }
                           ]
                       }
           }



    return  pack


def category_card_payload(user_id):
    category = ['Arcade', 'Puzzle & Logic', 'Sports & Racing', 'Strategy', 'Adventure', 'Action', 'Featured']
    from gif_Database import Action,Strategy,Adventure,Arcade,Puzzle,Sports
    from random import randint
    pack={ "users":[user_id],
           "message":{ "text": "Select your favourite category ",
                    "attachment":{ "type":"template",
                                      "payload":{ "template_type":"generic",
                                                  "elements":[ {
                                                                  "image_url":Action[randint(0,4)],
                                                                   "buttons": [{"title": "Action", 'type': "postback","payload": "Action"}]
                                                               },
                                                               # {   "image_url":Arcade[randint(0,4)],
                                                               #     "buttons": [{"title": "Arcade", 'type': "postback","payload": "Arcade"}]
                                                               #  },
                                                               {
                                                                  "image_url":Puzzle[randint(0,4)],
                                                                   "buttons": [{"title": "Puzzle & Logic", 'type': "postback","payload": "Puzzle & Logic"}]
                                                                },
                                                               {
                                                                  "image_url":Sports[randint(0,4)],
                                                                   "buttons": [{"title": "Sports & Racing", 'type': "postback","payload": "Sports & Racing"}]
                                                                },
                                                               {
                                                                  "image_url":Strategy[randint(0,4)],
                                                                   "buttons": [{"title": "Strategy", 'type': "postback","payload": "Strategy"}]
                                                                },
                                                               {
                                                                  "image_url":Adventure[randint(0,4)],
                                                                   "buttons": [{"title": "Adventure", 'type': "postback","payload": "Adventure"}]
                                                                },
                                                              # {
                                                              #     "image_url":"https://media.giphy.com/media/KgF61GMnMV6hlLiiaQ/giphy.gif",
                                                              #      "buttons": [{"title": "Featured", 'type': "postback","payload": "Featured"}]
                                                              # }
                                                               ]
                                                  }
                                      },
                       }
           }


    return pack

# {'code': 'Sk728YXJx',
#  'url': 'https://www.gamezop.com/g/Sk728YXJx?id=peSLSV',
#  'name': {'en': 'Pixel Slime'},
#  'isPortrait': False,
#  'description': {'en': 'Help this slimy green blob to jump over spikes and gaps to reach the exit in each level!'},
#  'gamePreviews': {'en': ''},
#  'assets': {'cover': 'https://static.gamezop.com/Sk728YXJx/cover.jpg',
#             'brick': 'https://static.gamezop.com/Sk728YXJx/brick.png',
#             'thumb': 'https://static.gamezop.com/Sk728YXJx/thumb.png',
#             'wall': 'https://static.gamezop.com/Sk728YXJx/wall.png',
#             'square': 'https://static.gamezop.com/Sk728YXJx/square.png',
#             'screens': ['https://static.gamezop.com/Sk728YXJx/game-1.png',
#                         'https://static.gamezop.com/Sk728YXJx/game-2.png',
#                         'https://static.gamezop.com/Sk728YXJx/game-3.png'],
#             'coverTiny': 'https://static.gamezop.com/Sk728YXJxcover-tiny.jpg',
#             'brickTiny': 'https://static.gamezop.com/Sk728YXJx/brick-tiny.png'},
#  'categories': {'en': ['Puzzle & Logic']},
#  'tags': {'en': ['Adventure', 'Fun', 'Arcade', 'Pixel', 'Minimal', 'Level-based', 'Difficult']},
#  'width': 800,
#  'height': 450,
#  'colorMuted': '#51582f',
#  'colorVibrant': '#5ca404',
#  'privateAllowed': False,
#  'rating': 4.5,
#  'gamePlays': 433750}
#
#
