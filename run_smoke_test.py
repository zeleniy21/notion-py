import argparse
import os
import sys

from notion.smoke_test import run_live_smoke_test

if __name__ == "__main__":
    description = "Run notion-py client smoke tests"
 parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
