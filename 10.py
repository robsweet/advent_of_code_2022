#!python
from pathlib import Path
import ipdb
import json


instructions = (
    Path("input_10.txt").read_text().strip().replace("addx", "noop\naddx").split("\n")
)
