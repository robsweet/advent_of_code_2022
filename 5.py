#!python
from copy import deepcopy
from pathlib import Path
import ipdb
import json
import re


def parse_move(my_move):
    qty, move_from, move_to = [
        int(e)
        for e in re.sub(f"move (\d+) from (\d+) to (\d)", r"\1,\2,\3", my_move).split(",")
    ]
    move_to -= 1
    move_from -= 1
    return [qty, move_from, move_to]


def parse_stacks(raw_stacks):
    raw_stacks = raw_stacks.split("\n")
    cols = int(re.sub(f".* (\d+)", r"\1", raw_stacks.pop()))

    stacks = []
    for col in range(cols):
        my_stack = []
        for tier in raw_stacks:
            position = 4 * col + 1
            letter = tier[position]

            if letter != " ":
                my_stack.append(letter)

        my_stack.reverse()
        stacks.append(my_stack)
    return stacks


raw_stacks, moves = Path("input_5.txt").read_text().split("\n\n")
stacks = parse_stacks(raw_stacks)
stacks2 = deepcopy(stacks)

for my_move in moves.strip().split("\n"):
    qty, move_from, move_to = parse_move(my_move)

    for i in range(qty):
        stacks[move_to].append(stacks[move_from].pop())

tops = [stack.pop() for stack in stacks]
print(f"Tops of the stacks are {''.join(tops)}")


# Part 2

for my_move in moves.strip().split("\n"):
    qty, move_from, move_to = parse_move(my_move)

    stacks2[move_to] += stacks2[move_from][-qty:]
    stacks2[move_from] = stacks2[move_from][0:-qty]

tops2 = [stack.pop() for stack in stacks2]
print(f"Tops of the stacks are {''.join(tops2)}")
