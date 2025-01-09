class HtmlNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("This method must be overridden by child classes")

    def props_to_html(self):
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __eq__(self, other):
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"



class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("LeafNode must have either a tag or a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value to render.")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("Parent must have either a tag.")
        if not children or not isinstance(children, list):
            raise ValueError("Parent must have a list of children.")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent must have a tag to render.")
        if not self.children:
            raise ValueError("Parent must have children to render.")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

