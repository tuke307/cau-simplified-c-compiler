class SLRTable:
    def __init__(self, slr_file):
        self.actions = {}
        self.goto = {}
        self._read_slr_table(slr_file)

    def _read_slr_table(self, slr_file):
        with open(slr_file, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                state = int(parts[0])
                symbol = parts[1]
                action = parts[2]
                if symbol.islower():  # Assuming lowercase are terminals
                    self.actions[(state, symbol)] = action
                else:
                    self.goto[(state, symbol)] = int(action)