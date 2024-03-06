class FiniteAutomaton:
    def __init__(self, _Q:list, _Sigma:list, _q0:str, _F:list,_delta:dict) -> None:
        self.Q = _Q
        self.Sigma = _Sigma
        self.delta = _delta
        self.q0 = _q0
        self.F = _F
        self.transition_table = self.create_transition_table()

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
        trans_table = {}
        for state in self.Q:
            trans_table[state]={}
            for char in self.Sigma:
                trans_table[state][char]=[]
        for element in self.delta:
            for state in element:
                for transition in element[state]:
                    resulting_state = element[state][transition]
                    trans_table[state][transition].append(resulting_state)
        return trans_table
    
    def print_trans_table(self):
        for state in self.transition_table:
            print(state, self.transition_table[state])