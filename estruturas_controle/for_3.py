#Dicionário
produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

#percorrendo chave de um dicionário
for chave in produto:
    print(chave)

#percorrendo valor de um dicionário
for valor in produto.values():
    print(valor)

#percorrendo chave e valor de um dicionário
for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave, valor)