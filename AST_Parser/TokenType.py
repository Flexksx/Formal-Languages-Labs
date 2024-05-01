import enum

class TokenType(enum.Enum):
    DOCUMENT_OPEN = 1
    DOCUMENT_CLOSE = 2
    TITLE_OPEN = 3
    TITLE_CLOSE = 4
    CHAPTER_OPEN = 5
    CHAPTER_CLOSE = 6
    SUBCHAPTER_OPEN = 7
    SUBCHAPTER_CLOSE = 8
    CONTENT = 9

    def __eq__(self, value: object) -> bool:
        return super().__eq__(value)