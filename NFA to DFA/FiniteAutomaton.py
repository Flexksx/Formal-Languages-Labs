class FiniteAutomaton:
    def __init__(self, Q=None, Sigma=None, q0=None, F=None, delta=None,create_trans:bool=True) -> None:
        self.Q = Q if Q is not None else []
        self.Sigma = Sigma if Sigma is not None else []
        self.q0 = q0 if q0 is not None else (self.Q[0] if self.Q else None)
        self.F = F if F is not None else []
        self.delta = delta if delta is not None else {}
        if create_trans is True:
            self.transition_table = self.create_transition_table()
        else: 
            self.transition_table = delta
        self.is_deterministic = self.is_deterministic()
        
        
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


    def is_deterministic(self):
        for state in self.transition_table:
            for transition in self.transition_table[state]:
                if len(self.transition_table[state][transition]) > 1:
                    return False
        return True