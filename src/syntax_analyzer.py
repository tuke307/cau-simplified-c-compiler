import argparse
from cfg import CFG
from slr_table import SLRTable
from token_parser import Parser
import os

CWD = os.getcwd()
CFG_FILE_PATH = os.path.join(CWD, "cfg.txt")
SLR_TABLE_FILE_PATH = os.path.join(CWD, "slr_table.csv")

def read_tokens(token_file):
    with open(token_file, "r") as file:
        tokens = file.read().strip().split()
    return tokens

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The token file to analyze")
    args = parser.parse_args()

    tokens = read_tokens(args.file)

    print(f"Tokens: {tokens}")
    print(f"CFG file: {CFG_FILE_PATH}")
    print(f"SLR Table file: {SLR_TABLE_FILE_PATH}")
    print("Parsing...")

    cfg = CFG(CFG_FILE_PATH)
    slr_table = SLRTable(SLR_TABLE_FILE_PATH)
    parser = Parser(cfg, slr_table)

    result = parser.parse(tokens)
    if result:
        print("Parse Tree:")
        print(result)
    else:
        print("Parsing failed.")
