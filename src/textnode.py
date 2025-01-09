from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, props=None):
        self.text = text
        self.text_type = text_type
        self.props = props if props is not None else {}

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.props == other.props)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.props})"
