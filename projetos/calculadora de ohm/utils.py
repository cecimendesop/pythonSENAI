def menu():
    print("Indique a operação:")
    print("1. Calcular Resistência (R)")
    print("2. Calcular Tensão (V)")
    print("3. Calcular Corrente (I)")
    print("4. Calcular Resistência para um Resistor")
    print("0. Sair")

def opcao():
    while True:
        try:
            opcao = int(input("Digite a opção escolhida: "))
            return opcao
        except ValueError:
            print("Opção inválida")

def solicita_tensao():
    while True:
        try:
            tensao = float(input("Digite a tensão (V): "))
            return tensao
        except ValueError:
            print("Digite apenas números")

def solicita_corrente():
    while True:
        try:
            corrente = float(input("Digite a corrente (I): "))
            return corrente
        except ValueError:
            print("Insira apenas números")

def solicita_resistencia():
    while True:
        try:
            resistencia = float(input("Digite a resistencia (R): "))
            return resistencia
        except ValueError:
            print("Insira apenas números")

def solicita_tensaofonte():
    while True:
        try:
            solicitatensaofonte = float(input("Digite a tensao da fonte (V): "))
            return solicitatensaofonte
        except ValueError:
            print("Insira apenas números")

def solicita_tensaoLED():
    while True:
        try:
            solicitatensaoLED = float(input("Digite a tensao da LED (V): "))
            return solicitatensaoLED
        except ValueError:
            print("Insira apenas números")

def solicita_correnteLED():
    while True:
        try:
            solicitacorrenteLED = float(input("Digite a corrente da LED (I): "))
            return solicitacorrenteLED
        except ValueError:
            print("Insira apenas números")

def solicita_resistor():
    while True:
        try:
            resistor = (solicita_resistencia() - solicita_tensaoLED() / solicita_correnteLED())
            return resistor
        except ValueError:
            print("Insira apenas números")



def calcular_resistencia():
    tensao = solicita_tensao()
    corrente = solicita_corrente()
    resistance = tensao / corrente
    print(f" o valor da resistência elétrica é de {resistance}")


def calcular_tensao():
    while True:
        try:
            resistencia = solicita_resistencia()
            corrente = solicita_corrente()
            tensao = resistencia * corrente
            print(f" o valor da tensao elétrica é de {tensao}")
            break
        except ValueError:
            print("Insira apenas números")



def calcular_corrente():
    while True:
        try:
            tensao = solicita_tensao()
            corrente = solicita_corrente()
            resistencia = tensao / corrente
            print(f"o valor da corrente elétrica é de {resistencia}")
            break
        except ValueError:
            print("Insira apenas números")

def calcular_resistor():
    while True:
        try:
            solicitatensaofonte = solicita_tensaofonte()
            solicitatensaoLED = solicita_tensaoLED()
            solicitacorrenteLED = solicita_correnteLED()
            resistor = solicita_resistor()
            print(f"o valor da resistencia do resistor é de {solicita_resistor()}")
            break
        except ValueError:
            print("Insira apenas números")



