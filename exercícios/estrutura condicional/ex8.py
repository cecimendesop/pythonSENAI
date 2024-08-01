rendabruta = input("Qual o valor da sua renda?: ")
while True:
    try:
        rendabruta = float(rendabruta)
        if rendabruta <= 56072:
            imposto = 0
            print(f"o resultado é de {imposto}")
        elif rendabruta <= 238532:
            imposto = (rendabruta - 56072) * 0.075
            print(f"o resultado é de {imposto}")
        elif rendabruta <= 522400:
            imposto = (238532 - 56072) * 0.075 + (rendabruta - 238532) * 0.15
            print(f"o resultado é de {imposto}")
        elif rendabruta <= 987600:
            imposto = (238532 - 56072) * 0.075 + (522400 - 238532) * 0.15 + (rendabruta - 522400) * 0.225
            print(f"o resultado é de {imposto}")
        else:
            imposto = (238532 - 56072) * 0.075 + (522400 - 238532) * 0.15 + (987600 - 522400) * 0.225 + (rendabruta - 987600) * 0.225
        print(f"Assim, o desconto do imposto de renda é de R$ {imposto:.2f} para uma renda bruta anual de R$ {rendabruta:.2f}")
        break
    except ValueError:
        print("Insira um número válido")
