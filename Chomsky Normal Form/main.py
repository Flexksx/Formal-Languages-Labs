from ChomskyNormalFormConverter import ChomskyNormalFormConverter
from Variant import Variant
from Grammar import Grammar



variant = Variant('/home/flexksx/Documents/Labs/LabsLFA/Chomsky Normal Form/variant.json')
production = variant.getP()
terminals = variant.getVT()
non_terminals = variant.getVN()
# print(production)
# print(terminals)
# print(non_terminals)

grammar = Grammar(terminals=terminals, non_terminals=non_terminals, productions=production)
converter = ChomskyNormalFormConverter(grammar)
converter.remove_epsilon_production()