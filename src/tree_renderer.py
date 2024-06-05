class TreeRenderer:
    """
    Class to render the parse tree.
    """

    @staticmethod
    def render_tree(node, prefix=""):
        """
        Render the parse tree.

        Parameters:
        node (Node): The root node of the parse tree.
        prefix (str): The prefix for the current level (used for indentation).
        """
        print(f"{prefix}{node.name}")
        children = getattr(node, 'children', [])
        for child in children:
            TreeRenderer.render_tree(child, prefix + "    ")
