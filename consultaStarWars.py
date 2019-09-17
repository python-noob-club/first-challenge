import requests
import json

print('Python noob club - First challenge\n')

fechar = 'noob'

while fechar != 'x':
    
    pesquisa = input('Search: ').lower()
  
    print('\n==================================================\n')

    r = requests.get('https://swapi.co/api/films/?search='+pesquisa)

    print('HTTP response:',r.status_code, '\n')

    dicionario = json.loads(r.text)

    print('==================================================\n')
    print(dicionario['count'], ' resultado(s).\n')

    for i in dicionario['results']:
        print('==================================================\n')
        print('Name:',i['title'])
        print('\nEpisode:',i['episode_id'])
        print('\nDirector:',i['director'])
        print('\nProducer:',i['producer'])
        print('\nRelease date:',i['release_date'])
        print('Opening crawl:',i['opening_crawl'])
        print('\n==================================================\n')

    fechar = input('Enter para continuar ou [x] para fechar.\n').lower()
