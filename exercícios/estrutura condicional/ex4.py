while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num1 > num2:
            print(f"O {num1} é maior que o {num2}")
        elif num2 > num1:
            print(f"O {num2} é maior que o {num1}")
        else:
            print("Os números são iguais")
        break
    except ValueError:
        print("Números inválidos, insira novamente")