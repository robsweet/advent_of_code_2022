#!python
from pathlib import Path
import ipdb
import json

trees = Path("input_8.txt").read_text().strip().split("\n")


def is_visible(target_x, target_y):
    target_height = int(trees[target_y][target_x])
    # print(f"Testing {target_x},{target_y} ({target_height})...")

    # print("\tLeft")
    # Left edge
    visible = True
    vis_left = True
    for x in range(0, target_x):
        # print(
        #     f"\t\tchecking {x},{target_y} >= {target_height} == {int(trees[target_y][x])} >= {target_height} == {not int(trees[target_y][x]) >= target_height}"
        # )
        if int(trees[target_y][x]) >= target_height:
            vis_left = False
            break

    # Top edge
    # print("\tTop")
    vis_top = True
    for y in range(0, target_y):
        # print(
        #     f"\t\tchecking {target_x},{y} >= {target_height} == {int(trees[y][target_x])} >= {target_height} == {not int(trees[y][target_x]) >= target_height}"
        # )
        if int(trees[y][target_x]) >= target_height:
            vis_top = False
            break

    # Right edge
    # print("\tRight")
    vis_right = True
    for x in reversed(range(target_x + 1, len(trees[0]))):
        # print(
        #     f"\t\tchecking {x},{target_y} >= {target_height} == {int(trees[target_y][x])} >= {target_height} == {not int(trees[target_y][x]) >= target_height}"
        # )
        if int(trees[target_y][x]) >= target_height:
            vis_right = False
            break

    # Bottom edge
    # print("\tBottom")
    vis_bot = True
    for y in reversed(range(target_y + 1, len(trees))):
        # print(
        #     f"\t\tchecking {target_x},{y} >= {target_height} == {int(trees[y][target_x])} >= {target_height} == {int(trees[y][target_x]) >= target_height}"
        # )
        if int(trees[y][target_x]) >= target_height:
            vis_bot = False
            break

    visible = vis_left or vis_top or vis_right or vis_bot
    # print(f"\n\t{vis_left}, {vis_top}, {vis_right}, {vis_bot} == {visible}\n")
    return visible


def visibility(target_x, target_y):
    target_height = int(trees[target_y][target_x])
    # print(f"Testing {target_x},{target_y} ({target_height})...")

    # print("\tLeft")
    # Left edge
    visible = True
    vis_left = 0
    for x in reversed(range(0, target_x)):
        vis_left += 1
        # print(
        #     f"\t\tchecking {x},{target_y} >= {target_height} == {int(trees[target_y][x])} >= {target_height} == {not int(trees[target_y][x]) >= target_height}"
        # )

        if int(trees[target_y][x]) >= target_height:
            break

    # Top edge
    # print("\tTop")
    vis_top = 0
    for y in reversed(range(0, target_y)):
        vis_top += 1
        # print(
        #     f"\t\tchecking {target_x},{y} >= {target_height} == {int(trees[y][target_x])} >= {target_height} == {not int(trees[y][target_x]) >= target_height}"
        # )
        if int(trees[y][target_x]) >= target_height:
            break

    # Right edge
    # print("\tRight")
    vis_right = 0
    for x in range(target_x + 1, len(trees[0])):
        vis_right += 1
        # print(
        #     f"\t\tchecking {x},{target_y} >= {target_height} == {int(trees[target_y][x])} >= {target_height} == {not int(trees[target_y][x]) >= target_height}"
        # )
        if int(trees[target_y][x]) >= target_height:
            break

    # Bottom edge
    # print("\tBottom")
    vis_bot = 0
    for y in range(target_y + 1, len(trees)):
        vis_bot += 1
        # print(
        #     f"\t\tchecking {target_x},{y} >= {target_height} == {int(trees[y][target_x])} >= {target_height} == {int(trees[y][target_x]) >= target_height}"
        # )
        if int(trees[y][target_x]) >= target_height:
            break

    visibility = vis_left * vis_top * vis_right * vis_bot
    # print(f"\n\t{vis_left}, {vis_top}, {vis_right}, {vis_bot} == {visibility}\n")
    return visibility


visible = (len(trees) * 2) + (len(trees[0]) * 2) - 4
for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[0]) - 1):
        if is_visible(x, y):
            visible += 1

print(f"Visible trees: {visible}")

max_vis = 0
for y in range(1, len(trees) - 1):
    for x in range(1, len(trees[0]) - 1):
        vis = visibility(x, y)
        max_vis = vis if vis > max_vis else max_vis

print(f"Max visibility: {max_vis}")
