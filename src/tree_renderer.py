class TreeRenderer:
    """
    Class to render the parse tree.
    """

    @staticmethod
    def render_tree(node, prefix="", is_last=True):
        """
        Render the parse tree.

        Parameters:
        node (Node): The root node of the parse tree.
        prefix (str): The prefix for the current level (used for indentation).
        is_last (bool): Whether the node is the last child of its parent.
        """
        # Determine the connector based on whether the node is the last child
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node.name}")

        # Prepare the prefix for the children
        if is_last:
            new_prefix = prefix + "    "
        else:
            new_prefix = prefix + "│   "

        # Render each child node
        children = getattr(node, 'children', [])
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            TreeRenderer.render_tree(child, new_prefix, is_last_child)
