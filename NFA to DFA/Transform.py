from NFA import NFA
from DFA import DFA

class TransformNFAtoDFA:
    def __init__(self, Q, Sigma, F, delta):
        self.nfa = NFA(Q, Sigma, F, delta)

