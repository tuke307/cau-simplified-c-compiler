class Node:
    """
    Node class for parse tree
    """

    def __init__(self, symbol, children=None):
        self.symbol = symbol
        self.children = children if children else []

    def __repr__(self):
        return f"Node({self.symbol}, {self.children})"