import re
from graphviz import Digraph
from Parser import Parser
from TokenType import TokenType
# Define the TokenType using an enumeration for clarity and robustness

TOKENS = [
    (TokenType.DOCUMENT_OPEN, r'\[document\]'),
    (TokenType.DOCUMENT_CLOSE, r'\[/document\]'),
    (TokenType.TITLE_OPEN, r'\[title\]'),
    (TokenType.TITLE_CLOSE, r'\[/title\]'),
    (TokenType.CHAPTER_OPEN, r'\[chapter\]'),
    (TokenType.CHAPTER_CLOSE, r'\[/chapter\]'),
    (TokenType.SUBCHAPTER_OPEN, r'\[subchapter\]'),
    (TokenType.SUBCHAPTER_CLOSE, r'\[/subchapter\]'),
    (TokenType.CONTENT, r'[^\[\]]*'),  # Match any content not containing '[' or ']'
]


def lexer(markdown):
    tokens = []
    while markdown:
        markdown = markdown.strip()
        match_found = False
        for token_type, token_regex in TOKENS:
            regex = re.compile(token_regex)
            match = regex.match(markdown)
            if match:
                value = match.group(0).strip()
                tokens.append((token_type, value))
                markdown = markdown[match.end():]
                match_found = True
                break
        if not match_found:
            raise SyntaxError(f'Unknown markdown: {markdown}')
    return tokens



def add_nodes_edges(tree, graph=None):
    if graph is None:
        graph = Digraph()
        graph.node(name=str(id(tree)), label=f'{tree.type.name}({tree.value})')

    for child in tree.children:
        child_label = f'{child.type.name}({child.value})' if child.value else child.type.name
        graph.node(name=str(id(child)), label=child_label)
        graph.edge(str(id(tree)), str(id(child)))
        graph = add_nodes_edges(child, graph)

    return graph




with open('AST_Parser/example.flexksx', 'r') as file:  
    code = file.read()

tokens = lexer(code)
parser = Parser()
ast = parser.parse(tokens)
graph = add_nodes_edges(ast)
graph.render('AST_Parser/result')