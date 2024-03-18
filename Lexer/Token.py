class Token:
    """
    Represents a token in a lexer.

    Attributes:
        - type (str): The type of the token.
        - value (str): The value of the token.
    """

    def __init__(self, type, value):
        self.type = type
        self.value = value
        
    def __repr__(self):
        return f"{self.type}"
    
    def __str__(self):
        return f"{self.type}"
    
    def __eq__(self, other):
        return self.type == other.type and self.value == other.value
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.type, self.value))
    
    def __lt__(self, other):
        return self.type < other.type and self.value < other.value
