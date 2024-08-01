print("Olá professor, insira duas notas para ter a média do aluno")
while True:
    try:
        nota1 = float(input("Insira a primeira nota do aluno: "))
        nota2 = float(input("Insira a segunda nota do aluno: "))
        if nota1 < 0 or nota1 > 100 and nota2 < 0 or nota2 > 100:
            print("Por favor, insira um valor entre 0 e 100")
        else:
            media = (nota1 + nota2) / 2
            print(f"O valor da média é de {media}")
            if media >= 70:
                print("O aluno está aprovado")
            else:
                print("O aluno está reprovado")

            break
    except ValueError:
        print("Por favor, insira notas válidas (apenas números)")
