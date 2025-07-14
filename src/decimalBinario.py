# criando desde deste momento um conversor de decimal para binário

numero = int(input("Digite um número decimal: "))   
numeroLista = []

for i in numero:
    if i.isnumeric(numero):
        numeroLista.append(int(i))
    else:
        print(f"{numero} deve ser binario.")

def deci
