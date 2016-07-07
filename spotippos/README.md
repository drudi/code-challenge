# Implementação da API para gerenciamento de imóveis em Spotippos

## Nota sobre a implementação

Conforme sugerido no enunciado do desafio, o backend de dados foi implementado somente na memória RAM, utilizando as estruturas de dados nativas da linguagem python. Embora seja possível manter as informações adicionadas (via POST) entre os requests, assim que o servidor é reiniciado, a base de dados volta ao estado inicial, que corresponde aos dados fornecidos nos arquivos properties.json e provinces.json

## Executando a API em modo desenvolvimento

Para executar a API em modo desenvolvimento, é necessário ter instalados o interpretador python versão 3.5+, o gerenciador de pacotes pip e o virtualenv, que possibilita a instalação de pacotes python em um ambiente isolado do resto do sistema.

Em um ambiente Linux ou MacOSX com os pacotes acima instalados, executar em um terminal:

```shell
$ git clone https://github.com/drudi/code-challenge.git
$ cd code-challenge
$ virtualenv -p `which python3` spotippos
$ cd spotippos
$ . bin/activate
$ pip install -r requirements.txt
$ python run.py

```

Se não ocorreu nenhum erro no processo, a seguinte saída deve ser observada no terminal onde os comandos foram executados:

```shell
(spotippos) localhost:spotippos user$ python run.py
Bottle v0.12.9 server starting up (using WSGIRefServer())...
Listening on http://localhost:8000/
Hit Ctrl-C to quit.

``

O ambiente de desenvolvimento estará então pronto para receber requisições na porta 8000. Para verificar se está tudo funcionando corretamente, basta acessar a seguinte URL no browser http://127.0.0.1:8000/hello, que deve retornar o número de propriedades atual.

## Executando a API em produção

TODO


