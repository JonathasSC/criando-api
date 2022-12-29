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

filmes = [
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
        'id': 3,
        'titulo': 'Vingadores: Guerra infinita',
        'diretor': 'Anthony Russo, Joe Russo'
    },
    {
        'id': 3,
        'titulo': 'Vingadores: Ultimato',
        'diretor': 'Anthony Russo, Joe Russo'
    },
    {
        'id': 4,
        'titulo': 'Homem-Aranha: De Volta ao Lar',
        'diretor': 'Jon Watts'
    },
]

# Consultar (todos)
@app.route('/filmes', methods=['GET'])
def obter_filmes():
    return jsonify(filmes)


# Consultar filmes por ID
@app.route('/filmes/<int:id>', methods=['GET'])
def obter_filme_por_id(id):
    for filme in filmes:
        if filme.get('id') == id:
            return jsonify(filme)


# Editar
@app.route('/filmes/<int:id>', methods=['PUT'])
def editar_filme_por_id(id):

    for indice,filme in enumerate (filmes):
        if filme.get('id') == id:
            filmes[indice].update(request.get_json())
            return jsonify(filmes[indice])

# Excluir

app.run(port=5000,host='localhost',debug=True)
