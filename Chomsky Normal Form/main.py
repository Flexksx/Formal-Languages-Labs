from ChomskyNormalFormConverter import ChomskyNormalFormConverter
from Variant import Variant
from Grammar import Grammar
from UnitTests import TestGrammar

variant = Variant(
    '/Users/cristiancretu/Documents/UniCode/LFA/Chomsky Normal Form/variant.json')
production = variant.getP()
terminals = variant.getVT()
non_terminals = variant.getVN()

grammar = Grammar(terminals=terminals,
                  non_terminals=non_terminals, productions=production)
converter = ChomskyNormalFormConverter(grammar)

print(grammar)

test = TestGrammar(grammar=grammar, converter=converter)
test.run()
print("All tests passed",end="\n\n")

new_grammar = converter.transform()
print(new_grammar)

