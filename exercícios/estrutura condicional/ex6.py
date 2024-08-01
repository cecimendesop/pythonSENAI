while True:
    try:
        num1 = int(input("Digite o primeiro numero inteiro: "))
        num2 = int(input("Digite o segundo numero inteiro: "))
        num3 = int(input("Digite o terceiro numero inteiro: "))
        if num1 > num2 and num1 > num3:
            print(f"{num1} é o maior entre os 3")
        elif num2 > num1 and num2 > num3:
            print(f"{num2} é o maior entre os 3")
        elif num3 > num1 and num3 > num2:
            print(f"{num3} é o maior entre os 3")
        else:
            print("Os 3 números são iguais")
        break
    except ValueError:
        print("Por favor digite apenas números inteiros")