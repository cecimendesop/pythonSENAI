while True:
    try:
        numeroentrada = input("Digite um número de 0 a 10 ou 0 a -10: ")
        numero = float(numeroentrada)
        if numero > 0 and numero <= 10:
            print("O número é positivo")
        elif numero < 0 and numero > (-10):
            print("O número é negativo")
        elif numero == 0:
            print("O número é zero")
        else:
            print("Número inválido")
        break
    except ValueError:
        print("Por favor, digite um número válido")