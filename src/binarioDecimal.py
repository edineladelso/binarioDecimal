# criando desde deste momento um conversor de decimal para binário

def receber_binario():
    while True:
        numero = input("binario: ")
        if '.' in numero:
            partes = numero.split('.')
            if len(partes) == 2 and all(partes[0]) and all(partes[1]) and \
               all(i in "01" for i in partes[0]) and all(i in "01" for i in partes[1]):
                return numero
            else:
                print("Erro! \tDigite apenas binários válidos (0 ou 1), com no máximo um ponto.")
        elif numero.isnumeric():
            if numero and all(i in "01" for i in numero):
                return numero
            else:
                print("Erro! \tDigite apenas binários (0 ou 1).")
        else:
            encerrar = input("Deseja encerrar o programa? (s/n): ")
            if encerrar.lower() == 's':
                print("======= Programa encerrado! =======")
                exit()

def criarLista(numero):
    return [int(i) for i in numero]

def binario_inteiro_para_decimal(numeroLista):
    return sum(bit * 2 ** exp for exp, bit in enumerate(reversed(numeroLista)))

def binario_fracionario_para_decimal(numero):
    if '.' not in numero:
        return binario_inteiro_para_decimal([int(i) for i in numero])
    parte_inteira, parte_fracionaria = numero.split('.')
    decimal_inteiro = binario_inteiro_para_decimal([int(i) for i in parte_inteira]) if parte_inteira else 0
    decimal_fracao = 0
    for idx, bit in enumerate(parte_fracionaria):
        decimal_fracao += int(bit) * (2 ** -(idx + 1))
    return decimal_inteiro + decimal_fracao

def main():
    print("======= Conversor de Binário para Decimal =======")
    while True:
        numero = receber_binario()
        if '.' in numero:
            print(f"Decimal: {binario_fracionario_para_decimal(numero)}")
        else:
            lista = [int(i) for i in numero]
            print(f"Decimal: {binario_inteiro_para_decimal(lista)}")

if __name__ == "__main__":
    main()
# Fim do código