print (dir (int))

print (dir (float))

a = 5
b = 2.5
print(a/b)

#is_integer : Esse valor é do tipo inteiro?
b.is_integer()

5.0.is_integer()

dir(int)
#Realiza uma soma
print(int.__add__(2, 3))

#Retorna o valor absoluto, valor positivo
print((-2).__abs__())

from decimal import Decimal, getcontext
#especificar quatro casas decimais
getcontext().prec = 4
Decimal(1) / Decimal(7)


