from utils import *

while True:
    menu()
    opcao = opcao()

    if opcao == 1:
        calcular_resistencia()
    elif opcao == 2:
        calcular_tensao()
    elif opcao == 3:
        calcular_corrente()
    elif opcao == 4:
        calcular_resistor()
    else:
        print("Programa finalizado")
    break


  
  