def solicitapeso():
  while True:
    try:
      solicitapeso = float(input("Digite em KG (quilos), o seu peso: "))
      altura = float(input("Digite sua altura em metros: "))
      imc = solicitapeso / (altura ** 2)
      print("O IMC é de:", imc)

      if imc < 18.5:
        print("Você está abaixo do peso")
      elif 18.5 <= imc <25:
        print("Você está com o peso adequado")
      elif 25 <= imc <30:
        print("Você está em sobrepeso")
      else:
        print("Nível de obesidade")
      break
    except ValueError:
      print("Insira apenas números")

solicitapeso()