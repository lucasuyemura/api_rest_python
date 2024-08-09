import jsonify

lista = list()

data = [[1,"Kabul","AFG","Kabol",1780000],[2,"Qandahar","AFG","Qandahar",237500]]

for linha in data:
    dados_formatados = {
        'id': linha[0],
        'Name': linha[1],
        'CountryCode': linha[2],
        'District': linha[3],
        'Population': linha[4]
    }

    lista.append(dados_formatados)


novo_dado = {
    'id':'Brazil',
     'Country': 'São Paulo',
     'zipcode': '04578000'
     }


print(novo_dado['id'])