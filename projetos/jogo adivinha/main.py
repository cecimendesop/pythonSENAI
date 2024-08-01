import random

print("BEM VINDO AO ADIVINHE O NUMERO MISTERIOSO!")
print("Um número de 1 a 100 está sendo gerado pelo jogo, e sua missão é descobrir o número gerado")
numero_aleatorio = random.randint(1, 10)
tentativas = 0

while True:
    try:
        chute = int(input("Digite o número que você acha que foi gerado: "))
        tentativas = tentativas + 1

        if chute < numero_aleatorio:
            print("Você está chutando muito baixo!")
        elif chute > numero_aleatorio:
            print("Você está chutando muito alto!")
        else:
            print("Parabéns! Você acertou o número.")

            jogador_novamente = input("Quer jogar novamente? (s/n): ")
            if jogador_novamente != "s":
                print("Fim de jogo!")
                break
    except ValueError:
            print("Por favor, digite apenas números!!!")





