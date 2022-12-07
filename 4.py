#!python
from pathlib import Path
import ipdb
import json

pairs = [pair.split(",") for pair in Path("input_4.txt").read_text().strip().split("\n")]

dupes = 0
intersections = 0

for pair in pairs:
    start1, stop1 = pair[0].split("-")
    set1 = set(range(int(start1), int(stop1) + 1))

    start2, stop2 = pair[1].split("-")
    set2 = set(range(int(start2), int(stop2) + 1))

    if set1.issubset(set2) or set2.issubset(set1):
        dupes += 1

    if len(set1 & set2) != 0:
        intersections += 1

print(f"Found {dupes} duplicate sets, {intersections} intersections")
