import requests
import json

def questions_by_Python():
    url = 'https://stackoverflow.com/questions'
    params = {'fromdate': '2022-07-18', 'min': '2022-07-20', 'tagged': 'python'}
    responce = requests.get(url, params=params )
    return responce.json()

print(questions_by_Python())