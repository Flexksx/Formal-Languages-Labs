from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammar
from copy import deepcopy
class Transformer:
    def __init__(self)->None:
        pass
    
    
    '''This part transforms the Grammar into a Finite Automation object,
    which can be used to check if a string belongs to the language of the grammar.
    It follows the algorithm presented by Mrs. Cojuhari at the course.'''
    def grammar_to_finite_automation(self, g:Grammar, q0:str, f:str)->FiniteAutomaton:
        Q = g.nonterminals
        Q.append("X")
        Sigma = g.terminals
        q0 = "S"
        F = ["X"]
        delta = {}
        '''The delta function is a dictionary of dictionaries,
        where the first key is the terminal'''
        for terminal in g.productions:
            for production in g.productions[terminal]:
                if len(production) > 1:
                    transition = production[0]
                    result_state = production[1]
                    if terminal not in delta:
                        delta[terminal] = {}
                    delta[terminal][transition] = result_state
                else:
                    transition = production
                    result_state = "X"
                    if terminal not in delta:
                        delta[terminal] = {}
                    delta[terminal][transition] = result_state
        return FiniteAutomaton(Q, Sigma, q0, F, delta)
    
    def finite_automaton_to_grammar(self, fa: FiniteAutomaton) -> Grammar:
        """
        Converts a finite automaton to a grammar.

        Args:
            fa (FiniteAutomaton): The finite automaton to be converted.

        Returns:
            Grammar: The resulting grammar.
        """
        nonterminals = fa.Q
        terminals = fa.Sigma
        productions = deepcopy(fa.transition_table)  # Make a copy to avoid modifying the original

        # Iterate over the dictionary and remove entries with empty lists
        for state, transitions in list(productions.items()):
            for symbol, resulting_states in list(transitions.items()):
                if not resulting_states:
                    del productions[state][symbol]

        return Grammar(nonterminals, terminals, productions)

    def NFA_to_DFA(self, nfa: FiniteAutomaton) -> FiniteAutomaton:
        """
        Converts a given NFA (Non-Deterministic Finite Automaton) to a DFA (Deterministic Finite Automaton).

        Args:
            nfa (FiniteAutomaton): The NFA to be converted.

        Returns:
            FiniteAutomaton: The converted DFA.

        Algorithm:
        1. Initialize the DFA states (Q_dfa) with the same states as the NFA.
        2. Initialize the DFA alphabet (Sigma_dfa) with the same alphabet as the NFA.
        3. Initialize the DFA initial state (q0_dfa) with the same initial state as the NFA.
        4. Initialize the DFA final states (F_dfa) with the same final states as the NFA.
        5. Initialize an empty dictionary to store the DFA transition table (delta_dfa).
        6. Create a queue to store the sets of states that need to be processed.
        7. For each state in Q_dfa and each symbol in Sigma_dfa, find the resulting state(s) in the NFA.
           - If the resulting state is a set of states, add it to the queue and update the transition table accordingly.
           - If the resulting state is a single state, update the transition table accordingly.
        8. Add the elements in the queue to Q_dfa.
        9. For each state in Q_dfa, create the delta function for each symbol in Sigma_dfa.
           - If the state is a single state, find the resulting state in the NFA and update the transition table accordingly.
           - If the state is a set of states, find the resulting state by taking the union of the resulting states of each state in the set.
        10. Convert Q_dfa to a list of strings.
        11. Return the converted DFA.

        Note: The algorithm assumes that the NFA has a transition table and follows the structure of the FiniteAutomaton class.
        """

        Q_dfa = deepcopy(nfa.Q)
        Sigma_dfa = nfa.Sigma
        q0_dfa = nfa.q0
        F_dfa = nfa.F
        delta_dfa = {}

        # Create the queue
        queue = []
        for state in Q_dfa:
            for symbol in Sigma_dfa:
                resulting_state = nfa.transition_table[state][symbol]
                if len(resulting_state) > 1:
                    queue.append(set(resulting_state))
                    nfa.transition_table[state][symbol] = set(resulting_state)
                nfa.transition_table[state][symbol] = set(resulting_state)

        # Put the queue in the Q_dfa too
        Q_dfa = [set([element]) for element in Q_dfa]
        for element in queue:
            Q_dfa.append(element)

        # Create the delta functions
        for state in Q_dfa:
            if len(state) <= 1:
                temp_state = list(state)[0]
                delta_dfa[temp_state] = {}
                for symbol in Sigma_dfa:
                    delta_dfa[temp_state][symbol] = {}
                    resulting_state = nfa.transition_table[temp_state][symbol]
                    if len(resulting_state) == 0:
                        resulting_state = ''
                    else:
                        resulting_state = ''.join(resulting_state)
                    delta_dfa[temp_state][symbol] = resulting_state
            elif len(state) > 1:
                temp_state = ''.join(state)
                delta_dfa[temp_state] = {}
                for symbol in Sigma_dfa:
                    delta_dfa[temp_state][symbol] = {}
                    resulting_state = set()
                    for element in state:
                        resulting_state = resulting_state.union(nfa.transition_table[element][symbol])
                    if len(resulting_state) == 0:
                        resulting_state = ''
                    else:
                        resulting_state = ''.join(resulting_state)
                    delta_dfa[temp_state][symbol] = resulting_state

        # Make Q_dfa a list of strings
        Q_dfa = [''.join(element) for element in Q_dfa]

        return FiniteAutomaton(Q_dfa, Sigma_dfa, q0_dfa, F_dfa, delta_dfa, create_trans=False)
