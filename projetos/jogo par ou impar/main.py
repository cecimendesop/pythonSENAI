import random
print("BEM VINDO AO JOGO DE PAR OU ÍMPAR")
print("1. Par")
print("2. Impar")
print("3. Sair")

while True:
    try:
        escolha_usuario = int(input("Você é 'par' ou 'impar' (1 para impar/ 2 para par):"))
        numero_de_usuario = int(input("Escolha um número :"))

        numero_computador = random.randint(1, 10)
        print("O número escolhido pelo computador é",numero_computador)

        soma = numero_computador + numero_de_usuario
        print("A soma é", soma)

        resultado = 'par' if soma % 2 == 0 else 'impar'
        print("A soma é", soma, "e o resultado é", resultado)

        if (escolha_usuario == 'par' and resultado) or (escolha_usuario == 'impar' and not resultado):
            print("Você perdeu!")
        else:
            print("Você ganhou!")
            jogar_novamente = input("Quer continuar jogando? (s/n): ")

        if jogar_novamente != "s":
            print("Fim do jogo")
            break

    except ValueError:
        print("O sistema apenas aceita números. Ex. 18")




