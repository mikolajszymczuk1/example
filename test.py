print("\t\tProgram do obliczania średniej artmetycznej.\n\n")

numbers_list = []

user_number = None
while user_number != "end":
    user_number = input("Podaj liczbę lub wpisz 'end' aby zakończyć : ")

    if user_number == "end":
        print("Pobieranie liczb zakończone !")

    try:
        numbers_list.append(int(user_number))

    except ValueError:
        print("\n\tZostała podana błędna wartość.\n")
