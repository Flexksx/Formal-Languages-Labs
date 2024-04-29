class StartOperation:
    """
    This class provides a static method to perform the start operation on a given set of productions.

    Args:
        P (dict, optional): The set of productions. Defaults to None.
        S (str, optional): The start symbol. Defaults to None.
        Vn (list, optional): The list of non-terminal symbols. Defaults to None.

    Returns:
        tuple: A tuple containing the updated set of productions, the updated start symbol, and the updated list of non-terminal symbols.
    """
    @staticmethod
    def do(P: dict = None, S: str = None, Vn: list = None):
        try:
            for value in P.values():
                for production in value:
                    for character in production:
                        if character == S:
                            raise ValueError('S is in a production')
        except:
            new_P = {'X': [S]}
            new_P.update(P)
            S = 'X'
            Vn.append(S)
            P = new_P

        return P, S, Vn
