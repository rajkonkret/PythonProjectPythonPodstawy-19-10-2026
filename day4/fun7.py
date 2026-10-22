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
