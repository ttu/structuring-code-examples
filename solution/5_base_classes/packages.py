import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__) + "..")
SOLUTION_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(SOLUTION_DIR)

from external_packages import *  # noqa: E402
