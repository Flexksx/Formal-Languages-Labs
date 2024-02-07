from Variant import Variant
from Grammar import Grammar

variant = Variant('/home/cristi/Documents/GitHub/LabsLFA/Lab1/variant.json')
VN = variant.getVN()
VT = variant.getVT()
P = variant.getP()

print(VN)
print(VT)
print(P)


grammar = Grammar(VN,VT,P)
print(grammar.generate_strings())
