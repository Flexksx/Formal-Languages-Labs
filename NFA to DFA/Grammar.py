import random
from FiniteAutomation import FiniteAutomation


class Grammar:
    def __init__(self, _VN: list, _VT: list, _P: dict) -> None:
        self.nonterminals = _VN
        self.terminals = _VT
        self.productions = _P

    '''
    This generates a string that belongs to the language of the grammar. If
    a terminal has more than one production, it will choose one at random.
    '''

    def generate_string(self, word="S") -> str:
        while (not self.word_is_terminal(word)):
            for char in word:
                if not self.char_is_terminal(char):
                    production = self.__pick_replacement(
                        self.productions[char])
                    word = word.replace(char, production)
        return word

    def word_is_terminal(self, word: str) -> bool:
        for char in word:
            if char in self.nonterminals:
                return False
        return True

    def char_is_terminal(self, char: str) -> bool:
        if char in self.nonterminals:
            return False
        return True

    def __pick_replacement(self, productions: list) -> str:
        return random.choice(productions)

    def generate_strings(self) -> list:
        ans = []
        while (len(ans) < 5):
            word = self.generate_string()
            if word not in ans:
                ans.append(word)
        return ans

    '''This part transforms the Grammar into a Finite Automation object,
    which can be used to check if a string belongs to the language of the grammar.
    It follows the algorithm presented by Mrs. Cojuhari at the course.'''

    def to_finite_automation(self):
        Q = self.nonterminals
        Q.append("X")
        Sigma = self.terminals
        q0 = "S"
        F = ["X"]
        delta = {}
        '''The delta function is a dictionary of dictionaries,
        where the first key is the terminal'''
        for terminal in self.productions:
            for production in self.productions[terminal]:
                if len(production) > 1:
                    transition = production[0]
                    result_state = production[1]
                    if terminal not in delta:
                        delta[terminal] = {}
                    delta[terminal][transition] = result_state
                else:
                    transition = production
                    result_state = "X"
                    if terminal not in delta:
                        delta[terminal] = {}
                    delta[terminal][transition] = result_state
        return FiniteAutomation(Q, Sigma, q0, F, delta)
