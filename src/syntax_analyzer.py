from cfg import CFG
from slr_table import SLRTable


class Parser:
    def __init__(self, cfg, slr_table):
        self.cfg = cfg
        self.slr_table = slr_table
        self.stack = []

    def parse(self, tokens):
        self.stack = [0]
        index = 0

        while index < len(tokens):
            state = self.stack[-1]
            token = tokens[index]

            if (state, token) in self.slr_table.actions:
                action = self.slr_table.actions[(state, token)]
                if action.startswith("s"):  # shift
                    self.stack.append(int(action[1:]))
                    index += 1
                elif action.startswith("r"):  # reduce
                    rule_index = int(action[1:])
                    lhs, rhs = self.cfg.rules[rule_index]
                    for _ in rhs:
                        self.stack.pop()
                    self.stack.append(self.slr_table.goto[(self.stack[-1], lhs)])
                elif action == "acc":
                    print("Parsing successful!")
                    return True
            else:
                print(f"Syntax error at token {token}")
                return False
        return False


if __name__ == "__main__":
    cfg = CFG("cfg.txt")
    slr_table = SLRTable("slr_table.txt")
    parser = Parser(cfg, slr_table)

    # read tokens from a file
    with open("tokens.txt", "r") as file:
        tokens = file.read().strip().split()

    result = parser.parse(tokens)
    print(f"Parsing result: {result}")
