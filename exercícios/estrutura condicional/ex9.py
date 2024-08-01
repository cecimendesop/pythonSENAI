import datetime
while True:
    try:
        tempo = datetime.datetime.now()
        dia = tempo.day
        mes = tempo.month
        ano = tempo.year
        diasemana = tempo.strftime("%A")
        if tempo.hour < 12:
            saudacao = "Good Morning!"
        elif 12 <= tempo.hour < 18:
            saudacao = "Good Afternoon!"
        else:
            saudacao = "Good Night!"
        frase = print(f" {saudacao} Today is {diasemana}, day {dia}, month {mes} from the year {ano}.")
        break
    except ValueError:
        print("Ocorreu um erro, tente novamente")

