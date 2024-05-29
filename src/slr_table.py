import csv

class SLRTable:
    def __init__(self, slr_file):
        self.actions = {}
        self.goto = {}
        self._read_slr_table(slr_file)

    def _read_slr_table(self, slr_file):
        with open(slr_file, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=';')
            headers = reader.fieldnames
            #print(f"CSV Headers: {headers}")  # Debug print to check headers

            for row in reader:
                state = int(row['State'])
                action_type = row['Goto']
                kernel = row['Kernel']
                closure = row['Closure']

                if action_type:  # Check if 'Goto' cell is not empty
                    if action_type.startswith('goto'):
                        # Extract symbol from the action_type like "goto(0, VDECL)"
                        symbol = action_type.split(",")[1].strip().strip(')')
                        target_state = int(action_type.split("(")[1].split(",")[0].strip())
                        self.goto[(state, symbol)] = target_state
                    else:
                        # This is an action entry (shift, reduce, or accept)
                        symbol = kernel.split("->")[1].strip().split()[0]
                        self.actions[(state, symbol)] = action_type.strip()

# Example usage
# slr_table = SLRTable('/mnt/data/slr_table.csv')
