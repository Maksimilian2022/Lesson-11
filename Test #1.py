import requests
def intelligent_request():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    hero_dict = {}
    responce = requests.get(url)
    hero_name = responce.json()

    for intelligent in hero_name:
        if intelligent.get('name') == 'Hulk':
            hero_dict['Hulk'] = intelligent['powerstats'].get('intelligence')
        elif intelligent.get('name') == 'Captain America':
            hero_dict['Captain America'] = intelligent['powerstats'].get('intelligence')
        elif intelligent.get('name') == 'Thanos':
            hero_dict['Thanos'] = intelligent['powerstats'].get('intelligence')
    print(hero_dict)



intelligent_request()


