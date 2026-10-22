def all_param(a, b, /, c=42, d=345):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_param(1, 2)  # a=1, b=2
all_param(1, 2, 4, 9)
# a=1, b=2
# c=4, d=9

all_param(1, 2, c=8)
# a=1, b=2
# c=8, d=345
all_param(1, 2, c=8, d=90)

# a=1, b=2
# c=8, d=90

# / oddziela pozycyjne od pozostałych
# TypeError: all_param() got some positional-only arguments passed as keyword arguments: 'a, b'
# all_param(a=1, b=4, c=9, d=100)
# a=1, b=4
# c=9, d=100
print(50 * "-")


def all_param_full(name, a, /, c=42, *args, d=67, **kwargs):
    print(f"{a=}, {name=}")  # tylko po pozycji
    print(f"{c=}, {d=}")  # tylko po pozycji
    print(f"{args=}, {kwargs=}")  # tylko po pozycji


all_param_full(1, 2)  # a=2, name=1
# all_param(1, b=2) # TypeError: all_param() got some positional-only arguments passed as keyword arguments: 'b'

all_param_full(1, 2, 4)
# a=2, name=1
# c=4, d=67
# args=(), kwargs={}
all_param_full(1, 2, c=4)
# a=2, name=1
# c=4, d=67
# args=(), kwargs={}

all_param_full(1, 2, 4, 5, 6, 7, 8, 9, 10, 11)  # jesli chcemy do args to c musi byc po pozycji
# a=2, name=1
# c=4, d=67
# args=(5, 6, 7, 8, 9, 10, 11), kwargs={}

all_param_full(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, d="radek")  # d musi byc po nazwie
# a=2, name=1
# c=4, d='radek'
# args=(5, 6, 7, 8, 9, 10, 11), kwargs={}

all_param_full(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, d="radek", imie="Tomek")
# a=2, name=1
# c=4, d='radek'
# args=(5, 6, 7, 8, 9, 10, 11), kwargs={'imie': 'Tomek'}

all_param_full(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, d="radek", imie="Tomek", name="Radek")
# a=2, name=1
# c=4, d='radek'
# args=(5, 6, 7, 8, 9, 10, 11), kwargs={'imie': 'Tomek', 'name': 'Radek'}
