import random

global infty
infty = 5


def or_operator(options: list[str] = None):
    symbol = random.choice(options)
    print(f'Choose {symbol}')
    return symbol


def plus_operator(symbol: str):
    init_symbol = symbol
    answer = ""
    last_i = 1
    for i in range(1, random.randint(1, infty)):
        answer += symbol
        last_i = i
    print(f'Repeat {init_symbol} {last_i} times')
    return answer


def star_operator(symbol: str):
    init_symbol = symbol
    answer = ""
    last_i = 0
    for i in range(0, random.randint(0, infty)):
        answer += symbol
        last_i = i
    print(f'Repeat {init_symbol} {last_i} times')
    return symbol


def question_operator(symbol: str):
    init_symbol = symbol
    if random.randint(0, 1) == 0:
        symbol = ""
        print(f'Empty {init_symbol}')
    else:
        print(f'Not Empty {init_symbol}')
    return symbol


def n_operator(symbol: str, n: int):
    for i in range(0, n):
        symbol += symbol
    print(f'Repeat {symbol} {n} times')
    return symbol


def const_operator(symbol: str):
    print(f'Constant {symbol}')
    return symbol


def first_regex():
    "O(P|Q|R)+2(3|4)"
    answer = ""
    answer += const_operator("O")
    choice = or_operator(["P", "Q", "R"])
    answer += plus_operator(choice)
    answer += "2"
    answer += or_operator(["3", "4"])
    return answer


def second_regex():
    "A*B(C|D|E)F(G|H|i)^2"
    answer = ""
    answer += star_operator("A")
    answer += const_operator("B")
    answer += or_operator(["C", "D", "E"])
    answer += const_operator("F")
    answer += n_operator(or_operator(["G", "H", "i"]), 2)
    return answer


def third_regex():
    "J+K(L|M|N)*O?(P|Q)^3"
    answer = ""
    answer += plus_operator("J")
    answer += const_operator("K")
    answer += star_operator(or_operator(["L", "M", "N"]))
    answer += question_operator("O")
    answer += n_operator(or_operator(["P", "Q"]), 3)
    return answer


print("-------First regex-------")
print(first_regex())
print("-------Second regex------")
print(second_regex())
print("-------Third regex-------")
print(third_regex())
