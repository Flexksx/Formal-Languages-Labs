from Grammar import Grammar
from FiniteAutomaton import FiniteAutomaton
from Variant import Variant

variant = Variant().getVariant()
Q=variant['Q']
Sigma=variant['Sigma']
F=variant['F']
delta=variant['delta']


fa = FiniteAutomaton(Q,Sigma,Q[0],F,delta)

print(fa.delta)
print(fa.print_trans_table())