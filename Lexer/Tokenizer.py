from Token import Token
import re


class Tokenizer:
    """
    A class that tokenizes a given line of code based on predefined tokens.

    Attributes:
        - tokens (list): A list of Token objects representing the predefined tokens.

    Methods:
        - tokenize(line): Tokenizes the given line of code and returns a list of tokens found.
        - get_tokens(): Returns the list of predefined tokens.
        - print_tokens(): Prints the list of predefined tokens.
    """

    def __init__(self):
        self.tokens = [
            Token("int", r"\bint\b"),
            Token("float", r"\bfloat\b"),
            Token("string", r"\bstring\b"),
            Token("bool", r"\bbool\b"),
            Token("true", r"\btrue\b"),
            Token("false", r"\bfalse\b"),
            Token("if", r"\bif\b"),
            Token("else", r"\belse\b"),
            Token("while", r"\bwhile\b"),
            Token("for", r"\bfor\b"),
            Token("return", r"\breturn\b"),
            Token("break", r"\bbreak\b"),
            Token("continue", r"\bcontinue\b"),
            Token("function", r"\bfun\b"),
            Token("print", r"\bprint\b"),
            Token("lparen", r"\("),
            Token("rparen", r"\)"),
            Token("lbrace", r"\{"),
            Token("rbrace", r"\}"),
            Token("lbracket", r"\["),
            Token("rbracket", r"\]"),
            Token("comma", r","),
            Token("semicolon", r";"),
            Token("colon", r":"),
            Token("dot", r"\."),
            Token("plus", r"\+"),
            Token("minus", r"-"),
            Token("multiply", r"\*"),
            Token("divide", r"/"),
            Token("modulus", r"%"),
            Token("assign", r"="),
            Token("equal", r"=="),
            Token("not_equal", r"!="),
            Token("greater", r">"),
            Token("less", r"<"),
            Token("greater_equal", r">="),
            Token("less_equal", r"<="),
            Token("quote", r'"'),
            Token("single_quote", r"'"),
            Token("and", r"&&"),
            Token("or", r"\|\|"),
            Token("not", r"!"),
            Token("identifier", r"[a-zA-Z_][a-zA-Z0-9_]*"),
            Token("int_literal", r"\d+"),
            Token("float_literal", r"\d+\.\d+"),
            Token("string_literal", r'".*"'),
            Token("comment", r'//.*')
        ]

    def tokenize(self, line):
        """
        Tokenizes the given line of code and returns a list of tokens found.

        Args:
            - line (str): The line of code to be tokenized.

        Returns:
            - list: A list of Token objects representing the tokens found in the line of code.
        """
        tokens_found = []
        index = 0  
        while index < len(line):
            match_found = False
            for token in self.tokens:
                pattern = re.compile(token.value)
                match = pattern.match(line, index)
                if match and match.start() == index:
                    tokens_found.append(token)
                    index = match.end()  
                    match_found = True
                    break  
            if not match_found:
                index += 1
        return tokens_found
    

    def get_tokens(self):
        """
        Returns the list of predefined tokens.

        Returns:
            - list: A list of Token objects representing the predefined tokens.
        """
        return self.tokens

    def print_tokens(self):
        """
        Prints the list of predefined tokens.
        """
        print(self.tokens)
