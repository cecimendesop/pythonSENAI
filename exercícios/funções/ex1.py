import datetime
def saudacao(nome):
    horaatual = datetime.datetime.now().hour
    if horaatual >= 0 and horaatual <= 5:
        print(f"Boa madruga, {nome}!")
    elif horaatual > 5 and horaatual <= 12:
        print(f"Bom dia, {nome}!")
    elif horaatual > 12 and horaatual <= 19:
        print(f"Boa tarde, {nome}!")
    else:
        print(f"Boa noite, {nome}!")


def solicitacao():
    nome = input("Digite o seu nome: ")
    return nome




saudacao (solicitacao())