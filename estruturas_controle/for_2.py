#Percorrendo uma string
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')
print('Fim')

#Percorrendo uma lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

#Percorrendo uma tupla
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

#Percorrendo um conjunto
for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)