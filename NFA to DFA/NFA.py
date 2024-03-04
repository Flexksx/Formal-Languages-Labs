import pandas as pd
from DFA import DFA
from FiniteAutomation import FiniteAutomation
class NFA(FiniteAutomation):
    def __init__(self, _Q, _Sigma, _F, _delta) -> None:
        self.Q = _Q
        self.Sigma = _Sigma
        self.F = _F
        self.delta = _delta
        self.states_nr = len(self.Q)
        self.transition_table= (self.create_transition_table())

    def __epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            current_state = stack.pop()
            epsilon_transitions = self.transition_table.get(current_state, {}).get('', [])
            for state in epsilon_transitions:
                if state not in closure:
                    closure.add(state)
                    stack.append(state)

        return sorted(list(closure))

    def nfa_to_dfa(self) -> DFA:
        dfa_Q = set()
        dfa_Sigma = self.Sigma
        dfa_delta = {}

        start_state = self.__epsilon_closure({'q0'})
        if start_state:
            dfa_Q.add(tuple(start_state))
            stack = [tuple(start_state)]
        else:
            stack = []

        while stack:
            current_states = stack.pop()
            dfa_delta[current_states] = {}

            for symbol in dfa_Sigma:
                next_states = []

                for state in current_states:
                    transitions = self.transition_table.get(state, {}).get(symbol, [])
                    next_states.extend(transitions)

                epsilon_closure_result = self.__epsilon_closure(next_states)
                if epsilon_closure_result:
                    state_key = tuple(epsilon_closure_result)

                    if state_key not in dfa_Q:
                        dfa_Q.add(state_key)
                        stack.append(state_key)

                    dfa_delta[current_states][symbol] = state_key

        return DFA(dfa_Q, dfa_Sigma, self.F, dfa_delta)
