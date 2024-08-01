def menu_calculadora():
    print("MENU PRINCIPAL")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisao")


menu_calculadora()

opcao = int(input("Escolha uma opcao: "))


def soma(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(numero1 + numero2)
    print("O resultado é: ", numero1 + numero2)


def subtracao(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(numero1 - numero2)
    print("O resultado é: ", numero1 - numero2)


def multiplicacao(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(numero1 * numero2)
    print("O resultado é ", numero1 * numero2)


def divisao(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(numero1 / numero2)
    print("O resultado é ", numero1 / numero2)


while True:
    try:
        if opcao == 1:
            soma(7, 2)
        elif opcao == 2:
            subtracao(4, 2)
        elif opcao == 3:
            multiplicacao(5, 2)
        elif opcao == 4:
            divisao(5, 2)
        else:
            print("Opcao invalida")
        break
    except ValueError:
        print("Opcao invalida")