import requests

api_key = 'd4e3edb1-ffb7-46a2-a0d3-bb130af73e3f'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'


res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
