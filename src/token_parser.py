from typing import List
from grammar import Grammar
from slr_table import SLRTable
from config import DEBUG
from node import Node
from tree_renderer import TreeRenderer


class Parser:
    """
    Parser class to parse tokens using SLR Table

    Usage:
    parser = Parser(grammar, slr_table)
    parse_tree = parser.parse(tokens)
    """

    def __init__(self, grammar: Grammar, slr_table: SLRTable):
        """
        Initialize Parser with Grammar and SLR Table.

        Parameters:
        grammar (Grammar): The grammar to be used for parsing.
        slr_table (SLRTable): The SLR parsing table.
        """
        self.grammar = grammar
        self.slr_table = slr_table
        self.stack = []
        self.tokens = []
        self.index = 0
        self.parse_tree = None

    def parse(self, tokens: List[str]) -> Node:
        """
        Parse tokens using SLR Table.

        Parameters:
        tokens (List[str]): The list of tokens to be parsed.

        Returns:
        Node: The root of the parse tree if parsing is successful, None otherwise.
        """
        self._initialize_parse(tokens)
        parse_tree_stack = []

        print(f"Parsing tokens: {tokens}")

        while True:
            state = self._current_state()
            token = self._current_token()

            if DEBUG:
                print(f"Current state: {state}, Current token: {token}")

            action = self._get_action(state, token)

            if DEBUG:
                print(f"Action: {action}")

            if not action:
                if token != "$": # Ignore $ token
                    self._handle_syntax_error(token)
                break

            if action.startswith("s"):
                self._shift(action, token, parse_tree_stack)
            elif action.startswith("r"):
                self._reduce(action, parse_tree_stack)
            elif action == "acc":
                return self._accept(parse_tree_stack)

        self._check_unfinished_parse(action)
        return None

    def _initialize_parse(self, tokens: List[str]):
        """
        Initialize the parsing process.

        Parameters:
        tokens (List[str]): The list of tokens to be parsed.
        """
        self.stack = [(0, None)]
        self.tokens = tokens + ["$"]
        self.index = 0
        self.parse_tree = None

    def _current_state(self) -> int:
        """
        Get the current state from the stack.

        Returns:
        int: The current state.
        """
        return self.stack[-1][0]

    def _current_token(self) -> str:
        """
        Get the current token from the tokens list.

        Returns:
        str: The current token.
        """
        return self.tokens[self.index]

    def _get_action(self, state: int, token: str) -> str:
        """
        Get the action from the SLR table for the given state and token.

        Parameters:
        state (int): The current state.
        token (str): The current token.

        Returns:
        str: The action to be taken.
        """
        return self.slr_table.actions.get(state, {}).get(token)

    def _handle_syntax_error(self, token: str):
        """
        Handle a syntax error.

        Parameters:
        token (str): The token where the syntax error occurred.
        """
        print(f"Syntax error at token number {self.index + 1}: {token}")

    def _shift(self, action: str, token: str, parse_tree_stack: List[Node]):
        """
        Perform a shift action.

        Parameters:
        action (str): The shift action.
        token (str): The current token.
        parse_tree_stack (List[Node]): The stack of parse tree nodes.
        """
        next_state = int(action[1:])
        self.stack.append((next_state, token))
        parse_tree_stack.append(Node(token))
        self.index += 1

    def _reduce(self, action: str, parse_tree_stack: List[Node]):
        """
        Perform a reduce action.

        Parameters:
        action (str): The reduce action.
        parse_tree_stack (List[Node]): The stack of parse tree nodes.
        """
        rule_index = int(action[1:])
        lhs, rhs = self.grammar.rules[rule_index]
        children = []

        for _ in rhs:
            self.stack.pop()
            children.insert(0, parse_tree_stack.pop())

        current_state = self._current_state()
        next_state = int(self.slr_table.goto[current_state][lhs])
        self.stack.append((next_state, lhs))

        parent_node = Node(lhs, children=children)
        parse_tree_stack.append(parent_node)

    def _accept(self, parse_tree_stack: List[Node]) -> Node:
        """
        Accept the input and return the parse tree.

        Parameters:
        parse_tree_stack (List[Node]): The stack of parse tree nodes.

        Returns:
        Node: The root of the parse tree.
        """
        self.parse_tree = parse_tree_stack[0]
        print("Parsing successful!")
        return self.parse_tree

    def _check_unfinished_parse(self, action: str):
        """
        Check if all tokens have been read but the accepting state has not been reached.

        Parameters:
        action (str): The last action taken.
        """
        if self.index == len(self.tokens) - 1 and action != "acc":
            print(
                "Error: All tokens have been read but the accepting state has not been reached."
            )

    def visualize_parse_tree(self):
        """
        Visualize the parse tree using the custom render_tree function.
        """
        if self.parse_tree:
            TreeRenderer.render_tree(self.parse_tree)
        else:
            print("No parse tree to visualize.")
