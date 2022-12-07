#!python
from pathlib import Path

lines = Path("input_2.txt").read_text().strip().split("\n")

ROUND_SCORE_KEY = {
    "A X": 4,  # A A (3 + 1)
    "A Y": 8,  # A B (6 + 2)
    "A Z": 3,  # A C (0 + 3)
    "B X": 1,  # B A (0 + 1)
    "B Y": 5,  # B B (3 + 2)
    "B Z": 9,  # B C (6 + 3)
    "C X": 7,  # C A (6 + 1)
    "C Y": 2,  # C B (0 + 2)
    "C Z": 6,  # C C (3 + 3)
}

total = sum(ROUND_SCORE_KEY[line] for line in lines)

ROUND_SCORE_KEY_2 = {
    "A X": 3,  # A C (0 + 3)
    "A Y": 4,  # A A (3 + 1)
    "A Z": 8,  # A B (6 + 2)
    "B X": 1,  # B A (0 + 1)
    "B Y": 5,  # B B (3 + 2)
    "B Z": 9,  # B C (6 + 3)
    "C X": 2,  # C B (0 + 2)
    "C Y": 6,  # C C (3 + 3)
    "C Z": 7,  # C A (6 + 1)
}

total2 = sum(ROUND_SCORE_KEY_2[line] for line in lines)

print(f"Total 1: {total}, Total 2: {total2}")
