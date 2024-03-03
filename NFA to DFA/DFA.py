import pandas as pd

class DFA:
    def __init__(self,_Q,_Sigma,_F,_delta) -> None:
        self.Q=_Q
        self.Sigma=_Sigma
        self.F=_F
        self.delta=_delta

    def print_transition_dict(self):
        for key in self.delta:
            print(key, self.delta[key])

    def print_transition_df(self):
        df = pd.DataFrame(self.delta)
        print(df.T)