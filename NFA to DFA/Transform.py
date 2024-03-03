from NFA import NFA
from DFA import DFA



class TransformNFAtoDFA:
    def __init__(self,Q,Sigma,F,delta)->None:
        self.nfa = NFA(Q,Sigma,F,delta)

    def nfa_to_dfa(self):
        dfa_Q = self.nfa.Q
        dfa_Sigma = self.nfa.Sigma
        dfa_delta={}
        return dfa_delta