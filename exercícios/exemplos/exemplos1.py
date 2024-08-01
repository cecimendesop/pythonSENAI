while True:
    try:
        idade = int(input('Digite sua idade: '))
        if idade > 0 and idade <= 100:
            print("idade:", idade)
            break
        else:
            print("idade invalida")
    except ValueError:
        print("digite sua idade em número. Ex: 17")