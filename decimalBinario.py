def receber_numero():
    while True:
        numero = input("decimal: ")
        try:
            valor = float(numero)
            if valor < 0:
                print("Erro! \tDigite apenas números positivos.")
                encerrar = input("Deseja encerrar o programa? (s/n): ")
                if encerrar.lower() == 's':
                    print("======= Programa encerrado! =======")
                    exit()
                continue
            return valor
        except ValueError:
            print("Erro! \tDigite apenas números (inteiros ou fracionários) positivos.")
            encerrar = input("Deseja encerrar o programa? (s/n): ")
            if encerrar.lower() == 's':
                print("======= Programa encerrado! =======")
                exit()

def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario

def fracionario_para_binario(numero, casas=10):
    inteiro = int(numero)
    fracao = numero - inteiro
    binario_inteiro = decimal_para_binario(inteiro)
    if fracao == 0:
        return binario_inteiro
    binario_fracao = ""
    count = 0
    while fracao > 0 and count < casas:
        fracao *= 2
        bit = int(fracao)
        binario_fracao += str(bit)
        fracao -= bit
        count += 1
    return f"{binario_inteiro}.{binario_fracao}"

def main():
    print("======= Conversor de Decimal para Binário =======")
    while True:
        numero = receber_numero()
        if numero == int(numero):
            print(f"Binário: {decimal_para_binario(int(numero))}")
        else:
            print(f"Binário: {fracionario_para_binario(numero)}")

if __name__ == "__main__":
    main()
# Fim do código
