# criando desde deste momento um conversor de decimal para binário
def receberNumero():
    while True:
        numero = input("binario: ")
        if numero.isnumeric():
            for i in numero:
                if i != "0" and i != "1":
                    print(f"Erro! \tDigite apenas binarios")
                else: return numero
        else:
            encerrar = input("Deseja encerrar o programa? (s/n): ")
            if encerrar.lower() == 's':
                print("======= Programa encerrado! =======")
                exit()

def criarLista(receber):
    numero = receber
    numeroLista = []
    for i in numero:
        if i.isnumeric():
            numeroLista.append(int(i))
        else:
            print(f"{numero} deve ser binario.")
            return None
    return numeroLista

def binario(criar):
    numeroLista = criar
    binario = 0
    contador = 0
    for i in numeroLista:
        binario += i*2**((len(numeroLista)-1)-contador)
        contador += 1
    return binario

def main():
    print("======= Conversor de Binário para Decimal =======")
    rodando = True
    while rodando:
        numero = receberNumero()
        lista = criarLista(numero)
        binario(lista)
        print(f"Decimal: {binario(lista)}")

if __name__ == "__main__":
    main()
# Fim do código