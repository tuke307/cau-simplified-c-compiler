class Grammar:
    def __init__(self, cfg_file, non_terminals_file, terminals_file):
        self.rules = []
        self._read_non_terminals(non_terminals_file)
        self._read_terminals(terminals_file)
        self.start_symbol = None
        self._read_cfg(cfg_file)

    def _read_non_terminals(self, file_path):
        with open(file_path, "r") as file:
            self.non_terminals = set(file.read().strip().split(", "))

    def _read_terminals(self, file_path):
        with open(file_path, "r") as file:
            self.terminals = set(file.read().strip().split(", "))

    def _read_cfg(self, cfg_file):
        print(f"Reading CFG from {cfg_file}")

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
                        if (
                            symbol not in self.non_terminals
                            and symbol not in self.terminals
                        ):
                            if symbol.islower():
                                self.terminals.add(symbol)
                            else:
                                self.non_terminals.add(symbol)
        self.start_symbol = self.rules[0][0]


# Example usage
# cfg = CFG('cfg.txt', 'non_terminals.txt', 'terminals.txt')
