class Node:
    def __init__(self, symbol, children=None):
        self.symbol = symbol
        self.children = children if children else []

    def __repr__(self):
        return f"Node({self.symbol}, {self.children})"

class Parser:
    def __init__(self, cfg, slr_table):
        self.cfg = cfg
        self.slr_table = slr_table
        self.stack = []
        self.tokens = []
        self.index = 0
        self.parse_tree = None

    def parse(self, tokens):
        self.stack = [0]
        self.tokens = tokens
        self.index = 0
        self.parse_tree = None
        parse_tree_stack = []

        while self.index < len(self.tokens):
            state = self.stack[-1]
            token = self.tokens[self.index]

            if (state, token) in self.slr_table.actions:
                action = self.slr_table.actions[(state, token)]
                if action.startswith("s"):  # shift
                    self.stack.append(int(action[1:]))
                    parse_tree_stack.append(Node(token))
                    self.index += 1
                elif action.startswith("r"):  # reduce
                    rule_index = int(action[1:])
                    lhs, rhs = self.cfg.rules[rule_index]
                    children = []
                    for _ in rhs:
                        self.stack.pop()
                        children.insert(0, parse_tree_stack.pop())
                    self.stack.append(self.slr_table.goto[(self.stack[-1], lhs)])
                    parse_tree_stack.append(Node(lhs, children))
                elif action == "acc":
                    self.parse_tree = parse_tree_stack.pop()
                    print("Parsing successful!")
                    return self.parse_tree
            else:
                print(f"Syntax error at token {token} at position {self.index + 1}")
                return None
        return None

# Example usage
# parser = Parser(cfg, slr_table)
# result = parser.parse(tokens)
# print(f"Parsing result: {result}")
