class Node:
    """
    A class representing a node in a tree structure.

    Attributes:
    name (str): The name of the node.
    parent (Node, optional): The parent node. Defaults to None.
    children (List[Node]): The list of child nodes.
    """

    def __init__(self, name, parent=None, children=None):
        """
        Initialize a Node instance.

        Parameters:
        name (str): The name of the node.
        parent (Node, optional): The parent node. Defaults to None.
        children (List[Node], optional): The list of child nodes. Defaults to None.
        """
        self.name = name
        self.parent = parent
        self.children = children if children is not None else []
        if parent:
            parent.children.append(self)
        for child in self.children:
            child.parent = self

    def __repr__(self):
        """
        Return a string representation of the Node instance.

        Returns:
        str: A string representation of the Node instance.
        """
        return f"Node('{self.name}')"
