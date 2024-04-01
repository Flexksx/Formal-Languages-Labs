import random

global infty
infty = 5


def or_operator(options: list[str] = None):
    answer = random.choice(options)
    print(f'Choose {answer} from {options}')
    return answer


def plus_operator(symbol: str):
    times = random.randint(1, infty)
    answer = symbol*times
    print(f'Repeat {symbol} {times} times')
    return answer


def star_operator(symbol: str):
    times = random.randint(0, infty)
    answer = symbol*times
    print(f'Repeat {symbol} {times} times')
    return answer


def question_operator(symbol: str):
    init_symbol = symbol
    if random.randint(0, 1) == 0:
        symbol = ""
        print(f'Empty {init_symbol}')
    else:
        print(f'Not Empty {init_symbol}')
    return symbol


def n_operator(symbol: str, n: int):
    answer = symbol*n
    print(f'Repeat {symbol} {n} times')
    return answer


def const_operator(symbol: str):
    print(f'Constant {symbol}')
    return symbol


def first_regex():
    "O (P|Q|R)+ 2 (3|4)"
    answer = ""
    answer += const_operator("O")
    answer += plus_operator(or_operator(["P", "Q", "R"]))
    answer += const_operator("2")
    answer += or_operator(["3", "4"])
    return answer


def second_regex():
    "A* B (C|D|E) F (G|H|i)^2"
    answer = ""
    answer += star_operator("A")
    answer += const_operator("B")
    answer += or_operator(["C", "D", "E"])
    answer += const_operator("F")
    answer += n_operator(or_operator(["G", "H", "i"]), 2)
    return answer


def third_regex():
    "J+ K (L|M|N)* O? (P|Q)^3"
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
