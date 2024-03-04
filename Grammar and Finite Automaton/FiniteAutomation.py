from Grammar import Grammar

class FiniteAutomation:
    def __init__(self) -> None:
        self.Q = []
        self.Sigma = []
        self.delta = {}
        self.q0 = ""
        self.F = []

    def __init__(self, _Q:list, _Sigma:list, _q0:str, _F:list,_delta:dict) -> None:
        self.Q = _Q
        self.Sigma = _Sigma
        self.delta = _delta
        self.q0 = _q0
        self.F = _F

    def string_belongs_to_language(self, string:str)->bool:
        state = self.q0
        for char in string:
            if char not in self.Sigma:
                return False
            if char in self.delta[state]:
                state = self.delta[state][char]
            else:
                return False
        return state in self.F

    def finite_automation_to_grammar(self):
        VN = self.Q
        VT = self.Sigma
        P = {}
        for state in self.delta:
            for symbol in self.delta[state]:
                if symbol not in P:
                    P[symbol] = []
                P[symbol].append(state + self.delta[state][symbol])
        return Grammar(VN, VT, P)