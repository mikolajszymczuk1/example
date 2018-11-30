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


def arithmetic_average(n_list):
    """ Funkcja zwraca średnia artmetyczna z list 'n_list'.

    >>> l = [1, 2, 3]
    >>> arithmetic_average(l)
    2
    >>> l.append(2)
    >>> arithmetic_average(l)
    2

    """

    return sum(n_list) / len(n_list)


input("Naciśnij dowolnu klawisz aby zakończyć. : ")
