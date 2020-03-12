#print(dir(str))
nome = 'Saulo Pedro'
print(nome)

doc = """Texto com múltiplas
    ...linhas"""
doc
print('Testo com múltiplas\n\t...linhas')
print (doc)

doc2 = '''Também é possível
...com 3 aspas simpleas'''
doc2

nome = "Ana Paula"
print(nome[0])
print(nome[6])
print(nome[-3]) #De trás pra frente(não começa com 0)
print(nome[4: ]) #A partir do 4 carctere em diante
print(nome[-5: ])
print(nome[:4])
print(nome[2:5])

numeros = '1234567890'
print(numeros[::])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])
print(nome[::-1])

#####
frase = 'Python é uma linguagem excelente'
'py' not in frase #Retorna verdadeiro porque o p está minúsculo
'ing' in frase
len(frase)
print(frase.lower()) #transformar a frase em letra minúscula
frase
frase = frase.upper() #maiúscula
frase
frase.split()
frase.split('E')

#dir(str)