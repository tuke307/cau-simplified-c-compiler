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
                line = line.strip()
                if not line:
                    continue
                lhs, rhs = line.split("->")
                lhs = lhs.strip()
                rhs_alternatives = rhs.split("|")
                for alternative in rhs_alternatives:
                    rhs_symbols = alternative.strip().split()
                    if rhs_symbols == ["''"]:  # Handle empty production
                        rhs_symbols = []
                    self.rules.append((lhs, rhs_symbols))
                    self.non_terminals.add(lhs)
                    for symbol in rhs_symbols:
                        if symbol.islower() and symbol not in ["vtype", "id", "assign", "semi", "literal", "character", "boolstr"]:
                            self.terminals.add(symbol)
                        elif symbol.isupper() or symbol in ["vtype", "id", "assign", "semi", "literal", "character", "boolstr"]:
                            self.non_terminals.add(symbol)
        self.start_symbol = self.rules[0][0]

# Example usage
# cfg = CFG('path_to_your_cfg_file.txt')
