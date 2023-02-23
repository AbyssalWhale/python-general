import requests
import config

GET_URL = "https://api.trello.com/1/members/me/boards"

RESPONSE = requests.get(GET_URL, params=config.AUTH_PARAMS)
BOARDS = RESPONSE.json()
for BOARD in BOARDS:
    print(BOARD["id"])
