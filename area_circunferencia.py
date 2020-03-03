from math import pi #módulo matemática

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == "__main__": #é nescessário chamar o módulo principal
    raio = input("Informe o raio: ")
    area = circulo(raio)
    print ("Área do circulo", area)
#pi = 3.14159
#raio = input("Informe o raio: ")
#print("Area do circulo", pi * float(raio) ** 2)