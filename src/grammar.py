from config import DEBUG
import os


class Grammar:
    """
    Context-Free Grammar class to represent CFG

    Usage:
    cfg = CFG('path_to_cfg.txt', 'path_to_non_terminals.txt', 'path_to_terminals.txt')
    """

    def __init__(self, cfg_file, non_terminals_file, terminals_file):
        self.rules = []
        self._read_non_terminals(non_terminals_file)
        self._read_terminals(terminals_file)
        self.start_symbol = None
        self._read_cfg(cfg_file)

    def _read_non_terminals(self, file_path):
        """
        Read non-terminals from a file
        """
        if DEBUG:
            print(f"Reading non-terminals from {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        try:
            with open(file_path, "r") as file:
                self.non_terminals = set(file.read().strip().split(", "))

            if DEBUG:
                print(f"Non-terminals: {self.non_terminals}\n{'-'*50}")
        except Exception as e:
            raise ValueError(
                f"An error occurred while parsing the file {file_path}: {str(e)}"
            )

    def _read_terminals(self, file_path):
        """
        Read terminals from a file
        """
        if DEBUG:
            print(f"Reading terminals from {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        try:
            with open(file_path, "r") as file:
                self.terminals = set(file.read().strip().split(", "))

            if DEBUG:
                print(f"Terminals: {self.terminals}\n{'-'*50}")
        except Exception as e:
            raise ValueError(
                f"An error occurred while parsing the file {file_path}: {str(e)}"
            )

    def _read_cfg(self, cfg_file):
        """
        Read CFG from a file
        """
        if DEBUG:
            print(f"Reading CFG from {cfg_file}")

        if not os.path.exists(cfg_file):
            raise FileNotFoundError(f"The file {cfg_file} does not exist.")

        try:
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
                    if DEBUG:
                        print(f"Processed rule: {lhs} -> {rhs_symbols}")
        except Exception as e:
            raise ValueError(
                f"An error occurred while parsing the file {cfg_file}: {str(e)}"
            )

        self.start_symbol = self.rules[0][0]

        if DEBUG:
            print(f"Start symbol: {self.start_symbol}\n{'-'*50}")
