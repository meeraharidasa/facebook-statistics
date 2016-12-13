import facebook
from src.get_token import read_token

import re

import urllib

ACCESS_TOKEN = read_token()
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='2.3')

try:
    identity = graph.get_object(id="me")
except facebook.GraphAPIError as e:
    print('Something went wrong:', e.type, e.message)

USER_ID = identity['id']
FIRST_NAME = identity['first_name']
LAST_NAME = identity['first_name']
USER_NAME = identity['name']
USER_GENDER = identity['gender']

INBOX_LIMIT = 0

try:
    inbox = graph.get_object(id=USER_ID, fields="inbox{to, comments}")
except facebook.GraphAPIError as e:
    print('Something went wrong:', e.type, e.message)

print("Last recent contact:")

for conversation_list in inbox['inbox']['data']:
    print(conversation_list['to']['data'][0]['name'])
