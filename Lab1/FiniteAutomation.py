class FiniteAutomation:
    def __init__(self) -> None:
        self.Q = []
        self.Sigma = []
        self.delta = {}
        self.q0 = ""
        self.F = []

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