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


def first_regex_gen():
    "O (P|Q|R)+ 2 (3|4)"
    answer = ""
    answer += const_operator("O")
    answer += plus_operator(or_operator(["P", "Q", "R"]))
    answer += const_operator("2")
    answer += or_operator(["3", "4"])
    return answer


def second_regex_gen():
    "A* B (C|D|E) F (G|H|i)^2"
    answer = ""
    answer += star_operator("A")
    answer += const_operator("B")
    answer += or_operator(["C", "D", "E"])
    answer += const_operator("F")
    answer += n_operator(or_operator(["G", "H", "i"]), 2)
    return answer


def third_regex_gen():
    "J+ K (L|M|N)* O? (P|Q)^3"
    answer = ""
    answer += plus_operator("J")
    answer += const_operator("K")
    answer += star_operator(or_operator(["L", "M", "N"]))
    answer += question_operator("O")
    answer += n_operator(or_operator(["P", "Q"]), 3)
    return answer


def parse_regex(regex):
    operators = ['+', '*', '?', '^']  # List of operators
    parentheses_stack = []
    parts = []

    current_part = ''

    for char in regex:
        if char == '(':
            if current_part:
                parts.append(current_part)
                current_part = ''
            parentheses_stack.append(len(parts))
        elif char == ')':
            if current_part:
                parts.append(current_part)
                current_part = ''
            start = parentheses_stack.pop()
            parts[start:] = [''.join(parts[start:])]
        elif char in operators:
            if current_part:
                parts.append(current_part)
                current_part = ''
            parts.append(char)
        else:
            current_part += char

    if current_part:
        parts.append(current_part)

    return parts


def compute_regex(parsed_regex: list[str] = None):
    if parsed_regex is None:
        return None
    indices_to_skip = []
    answer = ""
    skipped_simbols = ["(", ")", "*", "+", "?", "^"]
    for i in range(len(parsed_regex)):
        if i in indices_to_skip:
            continue
        part = parsed_regex[i]
        if part not in skipped_simbols:
            if "|" in part:
                current_token = or_operator(part.split("|"))
            else:
                current_token = part
                print(f"Current Token: {current_token}")
            if i+1 < len(parsed_regex):
                next_part = parsed_regex[i+1]
                if next_part == "*":
                    answer += star_operator(current_token)
                elif next_part == "+":
                    answer += plus_operator(current_token)
                elif next_part == "?":
                    answer += question_operator(current_token)
                elif next_part == "^":
                    power = int(parsed_regex[i+2])
                    answer += n_operator(current_token, power)
                    indices_to_skip.append(i+2)
                else:
                    answer += current_token
            else:
                answer += current_token
    return answer


regexes = ["O(P|Q|R)+2(3|4)", "J+K(L|M|N)*O?(P|Q)^3", "A*B(C|D|E)F(G|H|i)^2"]


for regex in regexes:
    print(f"Regex: {regex}")
    parsed_regex = parse_regex(regex)
    print(f"Parsed Regex: {parsed_regex}")
    print(f"Computed Regex: {compute_regex(parsed_regex)}")
    print("\n")
