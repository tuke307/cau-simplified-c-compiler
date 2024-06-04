from anytree import NodeMixin, RenderTree


class Node(NodeMixin):
    """
    Node class for parse tree, compatible with anytree
    """

    def __init__(self, symbol, parent=None, children=None):
        self.symbol = symbol
        self.parent = parent
        if children:
            self.children = children

    def __repr__(self):
        return f"Node({self.symbol})"
