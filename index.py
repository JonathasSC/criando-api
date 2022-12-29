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

movies = [
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
def GetMovieList():
    return jsonify(movies)


# Consultar filmes por ID
@app.route('/filmes/<int:id>', methods=['GET'])
def GetMovieByID(id):
    for movie in movies:
        if movie.get('id') == id:
            return jsonify(movie)


# Editar
@app.route('/filmes/<int:id>', methods=['PUT'])
def MovieEditByID(id):

    for indice,movie in enumerate (movies):
        if movie.get('id') == id:
            movies[indice].update(request.get_json())
            return jsonify(movies[indice])

# Criar 
@app.route('/filmes', methods=['POST'])
def AddMovie():
	new_movie = request.get_json()
	movies.append(new_movie)

	return jsonify(movies)
	
# Excluir
@app.route('/filmes/<int:id>', methods=['DELETE'])
def DeleteMovie(id):
	for indice, movie in enumerate(movies):
		if movie.get('id') == id:
			del movies[indice]
			
	return jsonify(movies)

app.run(port=5000,host='localhost',debug=True)
