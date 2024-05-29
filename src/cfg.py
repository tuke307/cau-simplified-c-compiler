class CFG:
    def __init__(self, cfg_file):
        self.rules = []
        self.non_terminals = set()
        self.terminals = set()
        self.start_symbol = None
        self._read_cfg(cfg_file)

    def _read_cfg(self, cfg_file):
        with open(cfg_file, "r") as file:
            for line in file:
                rule = line.strip().split("->")
                lhs = rule[0].strip()
                rhs = [r.strip() for r in rule[1].split("|")]
                self.rules.append((lhs, rhs))
                self.non_terminals.add(lhs)
                for symbol in rhs:
                    if symbol.islower():
                        self.terminals.add(symbol)
                    else:
                        self.non_terminals.add(symbol)
        self.start_symbol = self.rules[0][0]