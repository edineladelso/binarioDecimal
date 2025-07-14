# criando desde deste momento um conversor de decimal para binário

def receberNumero():
    while True:
        numero = input("binario: ")
        if numero.isnumeric():
            if numero and all(i in "01" for i in numero):
                return numero
            else: print("Erro! \tDigite apenas binários (0 ou 1).")
        else:
            encerrar = input("Deseja encerrar o programa? (s/n): ")
            if encerrar.lower() == 's':
                print("======= Programa encerrado! =======")
                exit()

def criarLista(numero):
    return [int(i) for i in numero]

def binario(numeroLista):
    return sum(bit * 2 ** exp for exp, bit in enumerate(reversed(numeroLista)))

def main():
    print("======= Conversor de Binário para Decimal =======")
    while True:
        numero = receberNumero()
        lista = criarLista(numero)
        print(f"Decimal: {binario(lista)}")

if __name__ == "__main__":
    main()
# Fim do código