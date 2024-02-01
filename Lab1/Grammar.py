import random

class Grammar:
    def __init__(self, _VN:list,_VT:list,_P:dict) -> None:
        self.nonterminals=_VN
        self.terminals=_VT
        self.productions=_P

    def generate_string(self, word="S")->str:
        while(not self.word_is_terminal(word)):
            for char in word:
                if not self.char_is_terminal(char):
                    # print(word)
                    production=self.pick_replacement(self.productions[char])
                    word = word.replace(char,production)
                    # print(production)
        return word


    def word_is_terminal(self,word:str)->bool:
        for char in word:
            if char in self.nonterminals:
                return False
        return True

    def word_is_terminal(self,word:list)->bool:
        for char in word:
            if len(char)>1:
                for ch in char:
                    if ch in self.nonterminals:
                        return False
            elif char in self.nonterminals:
                return False
        return True

    def char_is_terminal(self,char:str)->bool:
        if char in self.nonterminals:
            return False
        return True

    def pick_replacement(self,productions:list)->str:
        return random.choice(productions)


