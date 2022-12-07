#!python
from pathlib import Path
import json


def char_to_value(p):
    return (ord(p) - 64) if p < "a" else (ord(p) - 70)


packs = [
    (
        list(
            set(backpack[0 : int(len(backpack) / 2)])
            & set(backpack[int(len(backpack) / 2) :])
        )[0]
    )
    for backpack in Path("input_3.txt").read_text().strip().swapcase().split("\n")
]

pack_sum = sum([char_to_value(p) for p in packs])
print(f"Pack sum is {pack_sum}")

# Part 2
packs = Path("input_3.txt").read_text().strip().swapcase().split("\n")
badges = []
for i in range(int(len(packs) / 3)):
    badges.append(
        list(
            (set(packs[i * 3]) & set(packs[i * 3 + 1]))
            & (set(packs[i * 3 + 1]) & set(packs[i * 3 + 2]))
        )[0]
    )

badges = [char_to_value(p) for p in badges]

group_sum = sum(badges)
print(f"Group sum is {group_sum}")
