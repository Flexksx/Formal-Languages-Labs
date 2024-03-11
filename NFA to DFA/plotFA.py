from pyvis.network import Network


def plot_automaton(automaton):
    graph = Network(height="600px", width="100%", notebook=True, directed=True)

    for state, transitions in automaton.items():
        graph.add_node(state, label=state, color="green" if state == 'q3q2' else None, shape="doublecircle" if state == 'q3' else "circle")  # Set label and color for the state node
        for transition, next_state in transitions.items():
            if next_state:  # Skip transitions with an empty string
                graph.add_node(next_state, label=next_state, color="green" if next_state == 'q3q2' else None, shape="doublecircle" if next_state == 'q3q2' else "circle")  # Set label and color for the next state node
                graph.add_edge(state, next_state, label=transition)

    graph.show("automaton_graph.html")
