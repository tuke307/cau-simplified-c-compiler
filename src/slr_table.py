import csv


class SLRTable:
    """
    SLR Table class to read and store SLR Table from CSV files

    Usage:
    slr_table = SLRTable('path_to_lr_table_action.csv', 'path_to_lr_table_goto.csv')
    """

    def __init__(self, action_file: str, goto_file: str):
        """
        Initialize SLR Table from CSV files
        """
        self.actions = {}
        self.goto = {}
        self._read_action_table(action_file)
        self._read_goto_table(goto_file)

    def _read_action_table(self, action_file: str):
        """
        Read Action Table from a CSV file
        """
        print(f"Reading Action Table from {action_file}")

        with open(action_file, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=";")

            headers = reader.fieldnames
            print(f"CSV Headers: {headers}")  # Debug print to check headers

            for row in reader:
                state = int(row["State"])
                self.actions[state] = {
                    header: row[header] for header in headers if header != "State"
                }

    def _read_goto_table(self, goto_file: str):
        """
        Read Goto Table from a CSV file
        """
        print(f"Reading Goto Table from {goto_file}")

        with open(goto_file, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=";")

            headers = reader.fieldnames
            print(f"CSV Headers: {headers}")  # Debug print to check headers

            for row in reader:
                state = int(row["State"])
                self.goto[state] = {
                    header: row[header] for header in headers if header != "State"
                }
