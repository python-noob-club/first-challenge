import requests
import json
import sys



try:
    req = requests.get("https://swapi.co/api/films/")
except:
    print("ERRO DE CONEXÂO")
    exit()

filmes = json.loads(req.text)



def buscandoFilme(nome_filme):
    filme=""
    for i in filmes['results']:
        if(i['title'] == nome_filme):
            filme = i

    if filme != "":
        print(filme['title'])
        print('Titulo: ' + filme['title'])
        print('Diretor: ' + filme['director'])
        print('Produção: ' + filme['producer'])
        print('Data Lançamento: ' + filme['release_date'])
    else:
        print("Filme Não Encontrado, Tente Novamente")


filme = sys.argv


print(filme[1])
buscandoFilme(filme[1])













