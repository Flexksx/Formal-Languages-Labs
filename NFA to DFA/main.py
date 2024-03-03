from Variant import Variant
from Transform import TransformNFAtoDFA

variant = Variant().getVariant()

Q = variant['Q']
Sigma = variant["Sigma"]
F = variant["F"]
delta = variant["delta"]
sol = TransformNFAtoDFA(Q,Sigma,F,delta)
print(sol.nfa.df_trans_table())
print(sol.nfa_to_dfa())