while True:
    try:
        anonascimento = int(input('Digite o ano de nascimento da pessoa: '))
        anoatual = 2024
        idade = anoatual - anonascimento
        print(f"A pessoa tem {idade} anos e é {'maior' if idade >= 18 else 'menor'} de idade")
        break
    except ValueError:
        print("Digite um ano de nascimento válido")