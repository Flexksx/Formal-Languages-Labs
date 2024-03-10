from Grammar import Grammar
from Variant import Variant

variant = Variant('/home/flexksx/GitHub/LabsLFA/Grammar and Finite Automaton/variant.json')
terminals = variant.getVT()
nonterminals = variant.getVN()
productions = variant.getP()

grammar = Grammar(nonterminals, terminals, productions)
print(grammar.productions)
print(grammar.check_grammar_type())