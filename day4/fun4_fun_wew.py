# funkcja wewnętrzna zagnieżdżona
# uzywane w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2()  # wynik
    print(fun2)  # <function fun1.<locals>.fun2 at 0x0000015C139BF110>
    return fun2  # zwraca adres funkcji, referencje


xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000001E152C1F110>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
xFun()  # To jest fun2
xFun()  # To jest fun2
xFun()  # To jest fun2
