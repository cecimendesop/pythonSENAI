mesesano = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}
while True:
    try:
        numero = int(input("Digite um número de 1 a 12 (e qualquer outro para sair): "))
        if 1 <= numero <= 12:
            print("O mês correspondente é", mesesano[numero])
        else:
            print("Número correspondente inválido")
        break
    except ValueError:
        print("Por favor insira um número válido")