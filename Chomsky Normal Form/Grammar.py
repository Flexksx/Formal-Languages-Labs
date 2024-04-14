import random

class Grammar:
    def __init__(self, non_terminals:list[str] = None, terminals:list[str]=None,productions:dict[str]=None) -> None:
        self.nonterminals = non_terminals
        self.terminals = terminals
        self.productions = productions

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

    def check_grammar_type(self) -> str:
        """
        Determines the type of the grammar based on its productions.

        Returns:
            str: The type of the grammar. Possible values are:
                - 'Type 3 - Unrestricted' for grammars with unrestricted productions.
                - 'Type 2 - Context-free' for grammars with context-free productions.
                - 'Type 1 - Context-sensitive' for grammars with context-sensitive productions.
                - 'Type 0 - Regular' for grammars with regular productions.
        """
        # Check if all productions are in the form A -> a or A -> BC
        for nonterminal, production in self.productions.items():
            # print(nonterminal, production)
            if production == '':
                return 'Type 3 - Unrestricted'
            elif production[0] in self.nonterminals:
                if len(production) > 1:
                    if production[1] in self.terminals:
                        return 'Type 2 - Context-free'
                    elif production[1] in self.nonterminals:
                        return 'Type 1 - Context-sensitive'
        return 'Type 0 - Regular'