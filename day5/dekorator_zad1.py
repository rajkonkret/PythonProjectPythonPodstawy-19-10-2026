# dekorator - funkcja opakowująca inną funkcję

def dekorator(funk):
    def wew():
        print("Dekorujemy")
        funk()

    return wew  # zwracamy adres funkcji


@dekorator  # użycie dekoratora
def hej():
    print("Hej!!!")


hej()  # Hej!!!
