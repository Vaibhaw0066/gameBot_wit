
import requests
import  json

import re

data=requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en").json()
x='this is my minigolf court'
m='lf'
print((re.search(m,x)))

# "elements":[
#
#                                                                 { "title": 'Testing',
#                                                                  "subtitle":"",
#                                                                   "image_url":'https://media.giphy.com/media/xT0xeps3jsB0Y8XRPG/giphy.gif' ,
#                                                                    "buttons": [
#                                                                                { "title": "Preview", "type": "web_url", "url":'https://media.giphy.com/media/ZZqkQq4u1nI0aZ2LVF/giphy.gif' },
#                                                                                { "title": "Play", "type": "web_url", "url": 'https://www.gamezop.com/g/r1Xm38FQkl?id=peSLSV' }
#                                                                                ]
#                                                                 },
#             ]