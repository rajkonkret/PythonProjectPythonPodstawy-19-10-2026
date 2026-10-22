# dane nazwane, keywords

def connect(**opcje):
    print(opcje)
    print(type(opcje))  # <class 'dict'>

    name = opcje.get('name')
    print(name)  # Radek


connect()
connect(a=10)
connect(a=10, b=90)  # {'a': 10, 'b': 90}
connect(a=10, b=90, name="Radek")  # {'a': 10, 'b': 90, 'name': 'Radek'}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args(1, 2, 3, 4, 5, 6, name="Radek")
all_args(1, 2)
all_args(name="Radek")
# (1, 2, 3, 4, 5, 6) {'name': 'Radek'}
# (1, 2) {}
# () {'name': 'Radek'}
