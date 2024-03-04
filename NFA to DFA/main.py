from Variant import Variant
from Transform import TransformNFAtoDFA
from FiniteAutomation import FiniteAutomation
from NFA import NFA
from Grammar import Grammar

variant = Variant().getVariant()

Q = variant['Q']
Sigma = variant["Sigma"]
F = variant["F"]
delta = variant["delta"]
fa = FiniteAutomation(Q,Sigma,Q[0], F, delta)

grm = fa.to_grammar()
print(grm.productions)