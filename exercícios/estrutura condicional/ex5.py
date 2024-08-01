diassemana = {
    1: "Domingo",
    2: "Segunda-Feira",
    3: "Terça-Feira",
    4: "Quarta-Feira",
    5: "Quinta-Feira",
    6: "Sexta-Feira",
    7: "Sábado"
}
while True:
    try:
        numero = int(input("Digite um número de 1 a 7 (e qualquer outro para sair): "))
        if 1 <= numero <= 7:
            print("O dia correspondente é", diassemana[numero])
        else:
            print("Número correspondente inválido")
        break
    except ValueError:
        print("Por favor insira um número válido")