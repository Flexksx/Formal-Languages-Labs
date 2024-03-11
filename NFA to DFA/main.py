from Transformer import Transformer,FiniteAutomaton,Grammar
from Variant import Variant
from plotFA import plot_automaton

variant = Variant('/Users/cristiancretu/Documents/UniCode/LFA/NFA to DFA/variant.json').getVariant()
Q=variant['Q']
Sigma=variant['Sigma']
F=variant['F']
delta=variant['delta']


nfa = FiniteAutomaton(Q=Q,Sigma=Sigma,F=F,delta=delta)
transform = Transformer()

g=transform.finite_automaton_to_grammar(nfa)


# nfa.print_trans_table()
dfa = transform.NFA_to_DFA(nfa)
print(dfa.transition_table)


plot_automaton(dfa.transition_table)