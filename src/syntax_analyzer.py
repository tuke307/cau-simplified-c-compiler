import argparse
from grammar import Grammar
from slr_table import SLRTable
from token_parser import Parser
import os
from config import DEBUG

CWD = os.getcwd()
CFG_FILE_PATH = os.path.join(CWD, "files", "cfg.txt")
TERM_FILE_PATH = os.path.join(CWD, "files", "terminals.txt")
NON_TERM_FILE_PATH = os.path.join(CWD, "files", "non_terminals.txt")
LR_ACTION_TABLE_FILE_PATH = os.path.join(CWD, "files", "lr_table_action.csv")
LR_GOTO_TABLE_FILE_PATH = os.path.join(CWD, "files", "lr_table_goto.csv")


def read_tokens(token_file):
    """
    Read tokens from a file
    """
    if DEBUG:
        print(f"Reading tokens from {token_file}")

    if not os.path.exists(token_file):
        raise FileNotFoundError(f"The file {token_file} does not exist.")

    try:
        with open(token_file, "r") as file:
            tokens = file.read().strip().split()

        if DEBUG:
            print(f"Tokens: {tokens}\n{'-'*50}")

        return tokens
    except Exception as e:
        raise ValueError(
            f"An error occurred while parsing the file {token_file}: {str(e)}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The token file to analyze")
    args = parser.parse_args()

    tokens = read_tokens(args.file)

    grammar = Grammar(CFG_FILE_PATH, NON_TERM_FILE_PATH, TERM_FILE_PATH)
    slr_table = SLRTable(LR_ACTION_TABLE_FILE_PATH, LR_GOTO_TABLE_FILE_PATH)
    parser = Parser(grammar, slr_table)

    result = parser.parse(tokens)
    if result:
        parser.visualize_parse_tree()
