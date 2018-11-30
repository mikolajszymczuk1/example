def welcome_msg(msg):
    """ Funckja wyswitla komunikat wstepny/przywitalny. """

    print("\t\t", msg, "\n\n")


def create_numbers_list():
    """ Funkcja Pobierajaca liste liczb od uzytkownika. """

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

    return numbers_list


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


if __name__ == '__main__':
    input("Naciśnij dowolnu klawisz aby zakończyć. : ")
