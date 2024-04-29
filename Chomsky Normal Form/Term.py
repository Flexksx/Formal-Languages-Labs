class TermOperation:
    """
    A class that provides operations for transforming a grammar into Chomsky Normal Form.
    """

    @staticmethod
    def do(P: dict = None, S: str = None, Vn: list[str] = None, Vt: list[str] = None):
        """
        Transforms the given grammar into Chomsky Normal Form.

        Args:
            P (dict): The production rules of the grammar.
            S (str): The start symbol of the grammar.
            Vn (list[str]): The nonterminal symbols of the grammar.
            Vt (list[str]): The terminal symbols of the grammar.

        Returns:
            dict: The transformed grammar in Chomsky Normal Form.
        """
        new_P = TermOperation.replace_terminals_with_nonterminals(P, Vn, Vt)
        return new_P

    @staticmethod
    def replace_terminals_with_nonterminals(P: dict, Vn: list[str], Vt: list[str]) -> dict:
        """
        Replaces terminal symbols in the production rules with nonterminal symbols.

        Args:
            P (dict): The production rules of the grammar.
            Vn (list[str]): The nonterminal symbols of the grammar.
            Vt (list[str]): The terminal symbols of the grammar.

        Returns:
            dict: The grammar with terminal symbols replaced by nonterminal symbols.
        """
        terminal_to_nonterminal = {}
        new_P = P.copy()  # Initialize new_P with a copy of P
        for key, productions in P.items():
            new_productions = []
            for prod in productions:
                new_prod = TermOperation.replace_terminal(prod, Vt, terminal_to_nonterminal, Vn, new_P)
                new_productions.append(new_prod)
            new_P[key] = new_productions
        return new_P

    @staticmethod
    def replace_terminal(prod: str, Vt: list[str], terminal_to_nonterminal: dict, Vn: list[str], new_P: dict) -> str:
        """
        Replaces a terminal symbol with a nonterminal symbol.

        Args:
            prod (str): The production rule.
            Vt (list[str]): The terminal symbols of the grammar.
            terminal_to_nonterminal (dict): A mapping of terminal symbols to nonterminal symbols.
            Vn (list[str]): The nonterminal symbols of the grammar.
            new_P (dict): The grammar with terminal symbols replaced by nonterminal symbols.

        Returns:
            str: The production rule with terminal symbols replaced by nonterminal symbols.
        """
        new_prod = ''
        for char in prod:
            if char in Vt:
                if char not in terminal_to_nonterminal:
                    new_nt = TermOperation.__new_nonterminal(Vn)
                    Vn.append(new_nt)
                    terminal_to_nonterminal[char] = new_nt
                    new_P[new_nt] = [char]
                new_prod += terminal_to_nonterminal[char]
            else:
                new_prod += char
        return new_prod

    @staticmethod
    def __new_nonterminal(existing) -> str:
        """
        Generates a new nonterminal symbol.

        Args:
            existing: The existing nonterminal symbols.

        Returns:
            str: A new nonterminal symbol.
        
        Raises:
            ValueError: If all single-letter nonterminal symbols have been used.
        """
        for char in (chr(i) for i in range(65, 91)):
            if char not in existing:
                return char
        raise ValueError("Ran out of single-letter nonterminal symbols!")
