import csv
import os
from config import DEBUG


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
        if DEBUG:
            print(f"Reading Action Table from {action_file}")

        if not os.path.exists(action_file):
            raise FileNotFoundError(f"The file {action_file} does not exist.")

        try:
            with open(action_file, "r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file, delimiter=";")
                headers = reader.fieldnames

                if DEBUG:
                    print(f"CSV Headers: {headers}\n{'-'*50}")

                for row in reader:
                    state = int(row["State"])
                    self.actions[state] = {
                        header: row[header] for header in headers if header != "State"
                    }
        except Exception as e:
            raise ValueError(
                f"An error occurred while reading the file {action_file}: {str(e)}"
            )

    def _read_goto_table(self, goto_file: str):
        """
        Read Goto Table from a CSV file
        """
        if DEBUG:
            print(f"Reading Goto Table from {goto_file}")

        if not os.path.exists(goto_file):
            raise FileNotFoundError(f"The file {goto_file} does not exist.")

        try:
            with open(goto_file, "r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file, delimiter=";")
                headers = reader.fieldnames

                if DEBUG:
                    print(f"CSV Headers: {headers}\n{'-'*50}")

                for row in reader:
                    state = int(row["State"])
                    self.goto[state] = {
                        header: row[header] for header in headers if header != "State"
                    }
        except Exception as e:
            raise ValueError(
                f"An error occurred while reading the file {goto_file}: {str(e)}"
            )
