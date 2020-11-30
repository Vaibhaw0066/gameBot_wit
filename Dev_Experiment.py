import requests
import  json

import re

data=requests.get("https://pub.gamezop.com/v3/games?id=peSLSV&lang=en").json()
x='this is my minigolf court'
m='lf'
print((re.search(m,x)))