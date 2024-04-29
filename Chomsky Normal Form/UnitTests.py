from Grammar import Grammar
from ChomskyNormalFormConverter import ChomskyNormalFormConverter
from Start import StartOperation
from Bin import BinOperation
from Del import DelOperation
from Term import TermOperation
from Unit import UnitOperation
import unittest

class TestGrammar(unittest.TestCase):
    def __init__(self, grammar:Grammar=None, converter:ChomskyNormalFormConverter=None) -> None:
        self.grammar = grammar
        self.converter = converter
        
    def run(self):
        self.test_start()
        self.test_del()
        self.test_unit()
        self.test_bin()
        self.test_term()
        
    def test_start(self):
        P,S,Vn = self.grammar.productions, self.grammar.start_symbol, self.grammar.nonterminals
        new_P,new_S,new_Vn = StartOperation.do(P=P, S=S, Vn=Vn)
        for prod in new_P.values():
            self.assertNotIn(new_S, prod)
        print("START test passed")
        
    def test_del(self):
        P,S,Vn = self.grammar.productions, self.grammar.start_symbol, self.grammar.nonterminals
        new_P = DelOperation.do(P=P, S=S, Vn=Vn)
        for prod in new_P.values():
            self.assertNotIn("", prod)
        print("DEL test passed")
        
    def test_unit(self):
        P,Vn,Vt = self.grammar.productions, self.grammar.nonterminals, self.grammar.terminals
        new_P = UnitOperation.do(P=P, Vn=Vn, Vt=Vt)
        for prod in new_P.values():
            for production in prod:
                self.assertFalse(len(production) == 1 and production.isupper())
        print("UNIT test passed")
        
    def test_bin(self):
        P,Vn= self.grammar.productions, self.grammar.nonterminals
        new_P = BinOperation.do(P=P, Vn=Vn)
        for prod in new_P.values():
            for production in prod:
                self.assertTrue(len(production) <= 2)
        print("BIN test passed")
        
    def test_term(self):
        P,Vt,Vn,S = self.grammar.productions, self.grammar.terminals, self.grammar.nonterminals,self.grammar.start_symbol
        new_P = TermOperation.do(P=P, Vt=Vt,Vn=Vn,S=S)
        for prods in new_P.values():
            for prod in prods:
                if len(prod) > 1:
                    self.assertTrue(all(char in Vn for char in prod))

        print("TERM test passed")