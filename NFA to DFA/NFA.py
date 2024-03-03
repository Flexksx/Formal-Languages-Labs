import pandas as pd

class NFA:
    def __init__(self, _Q, _Sigma, _F, _delta) -> None:
        self.Q = _Q
        self.Sigma = _Sigma
        self.F = _F
        self.delta = _delta
        self.states_nr = len(self.Q)
        self.transition_table= (self.create_transition_table())


    def create_transition_table(self):
        transition_table = {}
        for state in self.Q:
            transition_table[state] = {}
            for symbol in self.Sigma:
                transition_table[state][symbol] = []
        for element in self.delta:
            for transition in element:
                init_state = transition
                key = list(element[transition].keys())[0]
                symbol = element[transition][key]
                transition_table[init_state][key].append(symbol)
        return transition_table


    def print_transition_df(self):
        df = pd.DataFrame(self.transition_table)
        print(df.T)

    def print_transition_dict(self):
        for state in self.transition_table:
            print(state, self.transition_table[state])