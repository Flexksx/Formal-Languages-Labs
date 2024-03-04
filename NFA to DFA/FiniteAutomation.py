import pandas as pd

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
        self.transition_table = (self.create_transition_table())
        self.is_deterministic = not self.is_non_deterministic()


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

    def is_non_deterministic(self):
        for state in self.transition_table:
            for symbol in self.transition_table[state]:
                if len(self.transition_table[state][symbol])>1:
                    return True
        return False

    def to_grammar(self):
        from Grammar import Grammar
        productions = []
        Vn = set()
        Vt = set(self.Sigma)
        productions={}
        for state in self.transition_table:
            productions[state] = {}
            for transition in self.transition_table[state]:
                productions[state][transition] = self.transition_table[state][transition]
        grammar = Grammar(Vn, Vt, productions)
        return grammar

