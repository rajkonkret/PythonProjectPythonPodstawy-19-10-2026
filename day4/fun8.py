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
