# dekorator - funkcja opakowująca inną funkcję

def dekorator(funk):
    def wew():
        print("Dekorujemy")
        return funk().upper()

    return wew  # zwracamy adres funkcji


@dekorator  # użycie dekoratora
def hej():
    # print("Hej!!!")
    return "Hej!!"


hej()  # Hej!!!
print(hej())  # HEJ!!

# zeby funkcja dekorator zaminiała wnik dziłania funkji na upper()
