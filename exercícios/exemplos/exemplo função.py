from datetime import datetime
def menu_calculadora():
    print("Calculadora")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
menu_calculadora()


def return_ola_nome(nome):
    return (f"Ola {nome}")

#Retorna o texto com "Olá Cecília"
    print("boa tarde return", return_ola_nome("Cecília"))

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

print("A sua idade é", calcular_idade(2007))

def exibir_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    print(f"{ano_atual} tem {idade} anos")


def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento: "))
            if ano_nascimento > datetime.now().year:
                print("Digite um ano válido")
            else:
                return ano_nascimento
        except ValueError:
            print("Digite um valor inteiro. Ex: 1997")


ano_nascimento = solicita_ano_nascimento()
exibir_idade(ano_nascimento = ano_nascimento)