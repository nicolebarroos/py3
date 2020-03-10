class Data: #Criando uma classe

    #Criando um construtor: Atribui um valor inicial aos atributos no momento da chamada
    def __init__(self, dia=2, mes=12, ano=2013):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def __str__(self): #definindo uma função pra ela
        return f'{self.dia}/{self.mes}/{self.ano}'

#Criando os objetos da classe
d1=Data(5, 12, 2010) 
#d1.dia = 5
#d1.mes = 12
#d1.ano = 2019
print(d1)

d2=Data(7, 4, 2012)
#d2.dia = 7
#d2.mes = 11
#d2.ano = 2020
print(d2)