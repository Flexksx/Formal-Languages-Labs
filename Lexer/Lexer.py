from FileReader import FileReader
from Tokenizer import Tokenizer

class Lexer:
    """
    The Lexer class is responsible for tokenizing input lines from a file.

    Args:
        - file_path (str): The path to the input file.

    Attributes:
        - lines (FileReader): An instance of the FileReader class to read lines from the file.
        - tokens (Tokenizer): An instance of the Tokenizer class to tokenize the lines.

    Methods:
        - tokenize(): Tokenizes each line from the file and prints the resulting tokens.
    """

    def __init__(self, file_path: str):
        self.lines = FileReader(file_path=file_path)
        self.tokens = Tokenizer()
        
    def tokenize(self):
        """
        Tokenizes each line from the file and prints the resulting tokens.
        """
        self.tokens = [self.tokens.tokenize(line) for line in self.lines.get()]
        
    def get_tokens(self):
        """
        Returns the list of predefined tokens.

        Returns:
            - list: A list of Token objects representing the predefined tokens.
        """
        self.tokenize()
        return self.tokens
    
    def print_tokens(self):
        """
        Prints the list of predefined tokens.
        """
        self.tokenize()
        for line in self.tokens:
            print(line)
        
