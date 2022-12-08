#!python
from pathlib import Path
import ipdb

lines = Path("input_1.txt").read_text()
elves = [
    sum([int(food) for food in elf.strip().split("\n")]) for elf in lines.split("\n\n")
]
winner_payload = max(elves)

combined_payload = sum(sorted(elves)[-3:])

print(f"winner_payload: {winner_payload}, combined_payload: {combined_payload}")
