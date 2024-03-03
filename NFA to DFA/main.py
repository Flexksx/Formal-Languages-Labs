from Variant import Variant
from Transform import TransformNFAtoDFA

variant = Variant().getVariant()

Q = variant['Q']
Sigma = variant["Sigma"]
F = variant["F"]
delta = variant["delta"]
sol = TransformNFAtoDFA(Q,Sigma,F,delta)
sol.nfa.print_transition_dict()
print()
dfa = sol.nfa_to_dfa()
dfa.print_transition_dict()