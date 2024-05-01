from TokenType import TokenType, enum


class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        type_name = self.type.name if isinstance(self.type, enum.Enum) else self.type
        return f"{type_name}({self.value}, {self.children})"

class Parser:
    def __init__(self):
        self.root = None
        self.current_node = None
        self.stack = []

    def parse(self, tokens):
        self.root = ASTNode(TokenType.DOCUMENT_OPEN, value="ROOT")
        self.current_node = self.root
        self.stack = [self.root]

        for token_type, value in tokens:
            self.handle_token(token_type, value)

        return self.root

    def handle_token(self, token_type, value):
        if token_type == TokenType.CHAPTER_OPEN:
            self.handle_chapter_open()
        elif token_type == TokenType.SUBCHAPTER_OPEN:
            self.handle_subchapter_open()
        elif token_type == TokenType.TITLE_OPEN:
            self.handle_title_open()
        elif token_type == TokenType.CONTENT:
            self.handle_content(value)
        elif token_type == TokenType.CHAPTER_CLOSE:
            self.handle_chapter_close()
        elif token_type == TokenType.SUBCHAPTER_CLOSE:
            self.handle_subchapter_close()
        elif token_type == TokenType.DOCUMENT_CLOSE:
            self.handle_document_close()

    def handle_chapter_open(self):
        chapter_node = ASTNode(TokenType.CHAPTER_OPEN)
        self.current_node.children.append(chapter_node)
        self.stack.append(chapter_node)
        self.current_node = chapter_node

    def handle_subchapter_open(self):
        subchapter_node = ASTNode(TokenType.SUBCHAPTER_OPEN)
        self.current_node.children.append(subchapter_node)
        self.stack.append(subchapter_node)
        self.current_node = subchapter_node

    def handle_title_open(self):
        title_node = ASTNode(TokenType.TITLE_OPEN)
        self.current_node.children.append(title_node)
        self.current_node = title_node

    def handle_content(self, content_value):
        self.current_node.children.append(ASTNode(TokenType.CONTENT, value=content_value))

    def handle_chapter_close(self):
        self.handle_close(TokenType.CHAPTER_OPEN)

    def handle_subchapter_close(self):
        self.handle_close(TokenType.SUBCHAPTER_OPEN)

    def handle_document_close(self):
        self.handle_close(TokenType.DOCUMENT_OPEN)

    def handle_close(self, expected_open_token):
        if self.stack and self.stack[-1].type == expected_open_token:
            self.stack.pop()
            if self.stack:
                self.current_node = self.stack[-1]
            else:
                print("Error: Stack is empty after popping.")
        else:
            print(f"Error: Mismatched {expected_open_token.name.lower()} close token.")
