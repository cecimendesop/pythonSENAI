
def converter_temperatura(celsius):
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin


def informar_temperatura():
    celsius = float(input('Informe a temperatura em celsius: '))
    return celsius


fahrenheit, kelvin = converter_temperatura(informar_temperatura())
print("Temperatura em Fahreinheit: ", fahrenheit)
print("Temperatura em Kelvin: ", kelvin)



