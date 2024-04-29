class BinOperation:
    """
    A class that performs binary operations on a given set of productions.

    Attributes:
        None

    Methods:
        do(P: dict[str, list[str]] = None, Vn: list[str] = None) -> dict[str, list[str]]:
            Performs the binary operation on the given set of productions.

        new_nonterminal(existing: list[str]) -> str:
            Generates a new nonterminal symbol.

    """

    @staticmethod
    def do(P: dict[str, list[str]] = None, Vn: list[str] = None) -> dict[str, list[str]]:
        """
        Performs the binary operation on the given set of productions.

        Args:
            P (dict[str, list[str]], optional): A dictionary representing the set of productions.
            Vn (list[str], optional): A list of nonterminal symbols.

        Returns:
            dict[str, list[str]]: The updated set of productions after performing the binary operation.

        Raises:
            None

        """
        if P is None or Vn is None:
            return {}

        existing_binaries = {}
        new_productions_dict = {}
        for key, productions in P.items():
            new_productions = []
            for production in productions:
                if len(production) > 2:
                    while len(production) > 2:
                        last_two = production[-2:]
                        if last_two not in existing_binaries:
                            new_nt = BinOperation.new_nonterminal(Vn)
                            Vn.append(new_nt)
                            new_productions_dict[new_nt] = [last_two]
                            existing_binaries[last_two] = new_nt
                        production = production[:-2] + existing_binaries[last_two]
                    new_productions.append(production)
                else:
                    new_productions.append(production)
            P[key] = new_productions
        P.update(new_productions_dict)
        return P
    
    @staticmethod
    def new_nonterminal(existing: list[str]) -> str:
        """
        Generates a new nonterminal symbol.

        Args:
            existing (list[str]): A list of existing nonterminal symbols.

        Returns:
            str: A new nonterminal symbol.

        Raises:
            ValueError: If there are no more single-letter nonterminal symbols available.

        """
        for char in (chr(i) for i in range(65, 91)):
            if char not in existing:
                return char
        raise ValueError("Ran out of single-letter nonterminal symbols!")
