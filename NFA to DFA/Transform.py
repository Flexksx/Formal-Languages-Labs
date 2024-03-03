from NFA import NFA
from DFA import DFA

class TransformNFAtoDFA:
    def __init__(self, Q, Sigma, F, delta):
        self.nfa = NFA(Q, Sigma, F, delta)

    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            current_state = stack.pop()
            epsilon_transitions = self.nfa.transition_table.get(current_state, {}).get('', [])
            for state in epsilon_transitions:
                if state not in closure:
                    closure.add(state)
                    stack.append(state)

        return sorted(list(closure))

    def nfa_to_dfa(self) -> DFA:
        dfa_Q = set()
        dfa_Sigma = self.nfa.Sigma
        dfa_delta = {}

        start_state = self.epsilon_closure({'q0'})
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
                    transitions = self.nfa.transition_table.get(state, {}).get(symbol, [])
                    next_states.extend(transitions)

                epsilon_closure_result = self.epsilon_closure(next_states)
                if epsilon_closure_result:
                    state_key = tuple(epsilon_closure_result)

                    if state_key not in dfa_Q:
                        dfa_Q.add(state_key)
                        stack.append(state_key)

                    dfa_delta[current_states][symbol] = state_key

        return DFA(dfa_Q, dfa_Sigma, self.nfa.F, dfa_delta)
