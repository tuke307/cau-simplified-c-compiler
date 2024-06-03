from typing import List, Tuple, Dict
from grammar import Grammar
from slr_table import SLRTable
from node import Node


class Parser:
    """
    Parser class to parse tokens using SLR Table

    Usage:
    parser = Parser(grammar, slr_table)
    parse_tree = parser.parse(tokens)
    """

    def __init__(self, grammar: Grammar, slr_table: SLRTable):
        """
        Initialize Parser with Grammar and SLR Table
        """
        self.grammar = grammar
        self.slr_table = slr_table
        self.stack = []
        self.tokens = []
        self.index = 0
        self.parse_tree = None

    def parse(self, tokens: List[str]):
        """
        Parse tokens using SLR Table
        """
        self.stack = [(0, None)]  # initialize stack with start state 0 and no symbol
        self.tokens = tokens + ["$"]  # add end-of-input marker
        self.index = 0
        self.parse_tree = None
        parse_tree_stack = []

        print(f"Parsing tokens: {tokens}")

        while True: # continue until we reach "acc" or encounter an error
            state = self.stack[-1][0]
            token = self.tokens[self.index]

            if token in self.slr_table.actions.get(state, {}):
                action = self.slr_table.actions[state][token]

                if action.startswith("s"):  # shift
                    next_state = int(action[1:])
                    self.stack.append(
                        (next_state, token)
                    )  # push the state and token to the stack
                    parse_tree_stack.append(Node(token))
                    self.index += 1

                elif action.startswith("r"):  # reduce
                    rule_index = int(action[1:])
                    lhs, rhs = self.grammar.rules[rule_index]
                    children = []

                    # pop the stack for the right-hand side of the rule
                    for _ in rhs:
                        self.stack.pop()
                        children.insert(0, parse_tree_stack.pop())

                    # push the left-hand side of the rule to the stack
                    current_state = self.stack[-1][0]
                    next_state = int(self.slr_table.goto[current_state][lhs])
                    self.stack.append((next_state, lhs))
                    parse_tree_stack.append(Node(lhs, children))

                elif action == "acc":  # accept
                    self.parse_tree = parse_tree_stack.pop()
                    print("Parsing successful!")
                    return self.parse_tree
            else:
                print(f"Syntax error at token {token} at position {self.index + 1}")
                return None
        return None
