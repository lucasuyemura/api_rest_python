from flask import Flask, jsonify, request, make_response
from bd import connect

# Inicia aplicação Flask

app = Flask(__name__)

# Passa função de conexão para variável para acessar criar o cursor do banco
connection_my_db = connect()
cursor = connection_my_db.cursor()


# Cria endpoint(city) para API 
@app.route('/city', methods=['GET'])
def listar_cidade():

    dados_formatados_em_json = list()

    cursor.execute('SELECT * FROM world.city')
    dados_retornados_na_consulta = cursor.fetchall()
    
    # Cria um loop para iterar sobre os dados que o banco retorna e formatar em um array de json
    for linha in dados_retornados_na_consulta:
        json = {
        'id': linha[0],
        'name': linha[1],
        'country_code': linha[2],
        'district': linha[3],
        'population': linha[4]
        }
    
        dados_formatados_em_json.append(json)

    # Retorna os dados formatados
    return jsonify(dados_formatados_em_json)


# Inserir novas cidades
@app.route('/city', methods=['POST'])
def inserir_cidade():
    
    novo_dado = request.json
    cursor.execute(f"INSERT INTO world.city(name, country_code, district, population) VALUES ('{novo_dado['name']}', '{novo_dado['country_code']}', '{novo_dado['district']}', {novo_dado['population']})")
    connection_my_db.commit()


    return jsonify(
        novo_dado
    )

# Excluir cidades
@app.route('/city', methods=['DELETE'])
def excluir_cidade():
    
    novo_dado = request.args.get('id')
    cursor.execute(f'DELETE FROM world.city WHERE id = {novo_dado}')

    # Necessário commit para refletir no banco de dados
    connection_my_db.commit()

    return {'message': 'Registro foi removido com sucesso!'}
    


# Atualizar cidades
@app.route('/city', methods=['PUT'])
def atualizar_cidade():

    novo_dado = request.get_json()
    cursor.execute(f"UPDATE world.city SET population = '{novo_dado['population']}' WHERE country_code = '{novo_dado['country_code']}'")

    # Necessário commit para refletir no banco de dados
    connection_my_db.commit()

    return novo_dado


# Roda aplicação
app.run()