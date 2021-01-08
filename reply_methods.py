
# Payload simple text message payload
def text_message_payload(user_id,message):
    text_messsage={"users":   [user_id],
               "message": {"text": message},
               }
    return text_messsage


#  Payload with quick reply
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


# Payload with text  message and two quick replies.
def msg_with_quick_reply_payload(user_id,msg,title1,title2):
    if title2=="":
        reply = {"users": [user_id], "message": {"text": msg,
                                                 "quick_replies":
                                                     [
                                                         {"content_type": "text",
                                                          "title": title1,
                                                          "payload": title1
                                                          }
                                                     ]
                                                 }
                 }
        return reply


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



# Payload for button linked with url
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

# Payloadd to send GIF
def GIF_payload(user_id,GIF):
    reply = {"users": [user_id], "message": {
                                            "attachment": {"type": "template",
                                                            "payload": {"template_type": "generic",
                                                            "elements": [{"image_url": GIF}]
                                                                        }
                                                            },
                                           }
                        }
    return reply

# https://media.giphy.com/media/QYkX9IMHthYn0Y3pcG/giphy.gif

# Payload to send multiple games provided in a list
def game_payload(user_id,game):

    from get_games import get_figures
    game=list(game)
    print(len(game)," games are sending")

    pack={ "users":[user_id],
           "message":{ "attachment":{ "type":"template",
                                      "payload":{ "template_type":"generic",
                                                  "elements":[ ]
                                                }
                                      },
                       }
           }

    for g in game:
        g = {"title": g['name']['en'],
             "subtitle": "Total game plays  " +str(get_figures(g['gamePlays'])),
             "image_url": g['assets']['cover'],
             "buttons": [{"title": "Preview", "type": "web_url", "url": str(g['gamePreviews']['en'])},
                         {"title": "Play", "type": "web_url", "url": g['url']}]
             }

        pack["message"]["attachment"]["payload"]["elements"].append(g)

    print("**********************************************************************************************************************************************")

    print(pack)
    print("**********************************************************************************************************************************************")

    return  pack


headers = {
    'api_token': 'API_TOKEN',
    'Content-Type': 'application/json',
}
#


# Payload to send categories
def category_card_payload(user_id):
    category = ['Arcade', 'Puzzle & Logic', 'Sports & Racing', 'Strategy', 'Adventure', 'Action', 'Featured']
    from gif_Database import Action,Strategy,Adventure,Arcade,Puzzle,Sports
    from random import randint
    pack={ "users":[user_id],
           "message":{
                    "attachment":{ "type":"template",
                                      "payload":{ "template_type":"generic",
                                                  "elements":[{
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
