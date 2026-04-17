class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        formatted_str = ""
        if self.props:
            for attribute in self.props:
                formatted_str += f' {attribute}="{self.props[attribute]}"'
            return formatted_str
        return None

    def __repr__(self):
        return f"HTMLNode: tag={self.tag}, value={self.value}, children={self.children}, props={self.props}."

    def __eq__(self, other):
        if (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        ):
            return True
        return False


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("value cannot be None.")

        if not self.tag:
            return f"{self.value}"

        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode: tag={self.tag}, value={self.value}, props={self.props}."


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag cannot be None.")

        if not self.children:
            raise ValueError("children cannot be None.")

        children = ""
        for child in self.children:
            children += child.to_html()

        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"

        return f"<{self.tag}>{children}</{self.tag}>"


if __name__ == "__main__":
    leaf = LeafNode("p", "ceci est un paragraphe")
    print(leaf)
