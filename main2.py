# 1. Criar uma api que disponibiliza a consulta, criação, edição e exclusão filmes

# 2. URL base - localhost

# 3. Endpoints - 
# 	localhost/filmes (GET)
# 	localhost/filmes/id (GET)
# 	localhost/filme/id (PUT)
# 	localhost/filme/id (DELETE)

# 4. Quais os recursos - Livros


from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Os Vingadores - The Avengers',
        'diretor': 'Joss Whedon'
    },
    {
        'id': 2,
        'titulo': 'Vingadores: Era de Ultron',
        'diretor': 'Joss Whedon'
    },
    {
        'id': 2,
        'titulo': 'Vingadores: Era de Ultron ',
        'diretor': 'Joss Whedon'
    },
    {
        'id': 3,
        'titulo': 'Vingadores: Era de Ultron ',
        'diretor': 'Joss Whedon'
    },
    {
        'id': 4,
        'titulo': 'Vingadores: Era de Ultron',
        'diretor': 'Joss Whedon'
    },
]
