from flask import Flask, jsonify, request # type: ignore

api_jogos = Flask(__name__)

jogos = [
    {
        'id': 1,
        'título': 'Grand Theft Auto 5',
        'autor': 'Rockstar Games'
    },
    {
        'id': 2,
        'título': 'League of Legends',
        'autor': 'Riot Games'
    },
    {
        'id': 3,
        'título': 'Rainbow Six Siege',
        'autor': 'Ubisoft'
    }
]

# obter todos os jogos
@api_jogos.route('/jogos', methods=['GET'])
def obter_jogos():
    return jsonify(jogos)

# obter por id
@api_jogos.route('/jogos/<int:id>', methods=['GET'])
def obter_jogo_por_id(id):
    for jogo in jogos:
        if jogo.get('id') == id:
            return jsonify(jogo)

# editar jogo
@api_jogos.route('/jogos/<int:id>', methods=['PUT'])
def editar_jogo(id):
    jogo_alterado = request.get_json()
    for indice,jogo in enumerate(jogos):
        if jogo.get('id') == id:
            jogos[indice].update(jogo_alterado)
            return jsonify(jogos[indice])

# adicionar novo jogo
@api_jogos.route('/jogos', methods=['POST'])
def adicionar_jogo():
    novo_jogo = request.get_json()
    jogos.append(novo_jogo)
    return jsonify(jogos)

# deletar jogo
@api_jogos.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    for indice, jogo in enumerate(jogos):
        if jogo.get('id') == id:
            del jogos[indice]
            return jsonify(jogos)

api_jogos.run(port=5500, host='localhost', debug=True)