class DFA:
    def __init__(self,_Q,_Sigma,_F,_delta) -> None:
        self.Q=_Q
        self.Sigma=_Sigma
        self.F=_F
        self.delta=_delta