# Desafio!
O desafio consiste em fazer um programa em Python onde o usuário irá entrar no promopt (eu prefiro e recomendo o Cmder para usuários do Windows).


# Descrição em BDD (Behavior Driven Development)

  
 **Funcionalidade**: Listagem de informações de meu(s) filme(s) preferidos dentro da série 'Star Wars'

&nbsp;&nbsp;&nbsp;&nbsp;Como um usuário do sistema

&nbsp;&nbsp;&nbsp;&nbsp;Do meu computador

&nbsp;&nbsp;&nbsp;&nbsp;Eu quero entrar com uma lista de um ou mais filmes da saga 'Star Wars'; Exemplo: **"consultaStarWars.py (espaço) 'The Last Hope'"**

&nbsp;&nbsp;&nbsp;&nbsp;Então deverá ser exibido na tela as informações deste(s) filme(s); Exemplo: **"diretor, ano de lançamento e sinopse"**
  
 
## Descrição em TDD (Test Driven Development)

&nbsp;&nbsp;&nbsp;&nbsp; **Cenário:** Sucesso na transmissão da listagem de filmes

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  **Dado** que o usuário faça uma requisição

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **Quando** o sistema receber o JSON de resposta

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **Entao** o código de status de resposta deve ser igual a 200

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; **Entao** o sistema deve exibir mensagem "HTTP response: 200 (ok)!"

  
**Cenário:** Sucesso na exibição dos dados

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**Dado** a lista de todos os filmes de Star Wars

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**Então** o sistema deve exibir somente as informações de meu(s) filme(s) predileto(s)


## Ferramentas de suporte

**Cmder**
&nbsp;&nbsp;&nbsp;&nbsp; https://cmder.net/

**Star Wars Movies Database API**
&nbsp;&nbsp;&nbsp;&nbsp;https://swapi.co/

**JSON Python lib**
&nbsp;&nbsp;&nbsp;&nbsp;https://docs.python.org/3/library/json.html


**Requests Python lib**
&nbsp;&nbsp;&nbsp;&nbsp;https://docs.python.org/3/library/json.html

## Dicas para pesquisa
Os sites das respectivas bibliotecas já contém exemplos práticos.

Outra dica é ir digitando os dados direto no no navegador o endereço **Star Wars Movies Database API** e observando o resultado. No final das contas a o nosso programa  vai fazer exatamente a mesma coisa, só que quem vai fazer isto para nós será o Python e - melhor.

## Como eu costumo fazer
**Para iniciantes:** no próprio Cmder ou IDLE, eu vou digitando os comandos e testando linha por linha para ver se funciona. Depois pego essas linhas e coloco no meu código.

**Para quem já tem um pouco mais de prática/confiança :** outra opção é fazer pequenas partes do código e ir rodando para ver se fuciona (esta é para quem tem mais confiança). A cada novo trecho de código, executa, vê o resultado e ajusta.

Boa sorte e tamo junto!
Noobs.
