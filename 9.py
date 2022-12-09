#!python
from pathlib import Path
import ipdb
import json
from copy import copy

# from Math import abs

moves = Path("input_9.txt").read_text().strip().split("\n")


class Mover:
    def __init__(self, num_tail_segments):
        self.head = {"x": 0, "y": 0}
        self.tail = [{"x": 0, "y": 0} for i in range(num_tail_segments)]
        self.tail_positions = ["0,0"]

    def positions(self):
        tail_positions = [f"{seg['x']},{seg['y']}" for seg in self.tail]
        return f"Head: {self.head['x']},{self.head['y']}  Tails: {tail_positions}"

    def move_head(self, direction):
        if direction == "R":
            self.head["x"] += 1
        elif direction == "L":
            self.head["x"] -= 1
        elif direction == "U":
            self.head["y"] += 1
        elif direction == "D":
            self.head["y"] -= 1

    def move_tail(self):
        previous_segment = self.head
        for idx, tail_segment in enumerate(self.tail):
            if (
                abs(previous_segment["x"] - tail_segment["x"]) < 2
                and abs(previous_segment["y"] - tail_segment["y"]) < 2
            ):
                pass

            else:
                if previous_segment["x"] == tail_segment["x"]:
                    #  Straight vertical move
                    if previous_segment["y"] > tail_segment["y"]:
                        tail_segment["y"] += 1
                    else:
                        tail_segment["y"] -= 1
                elif previous_segment["y"] == tail_segment["y"]:
                    #  Straight horizontal move
                    if previous_segment["x"] > tail_segment["x"]:
                        tail_segment["x"] += 1
                    else:
                        tail_segment["x"] -= 1

                else:
                    if (
                        previous_segment["y"] > tail_segment["y"]
                        and previous_segment["x"] > tail_segment["x"]
                    ):
                        #  Diagonal move NE
                        tail_segment["x"] += 1
                        tail_segment["y"] += 1

                    elif (
                        previous_segment["y"] < tail_segment["y"]
                        and previous_segment["x"] > tail_segment["x"]
                    ):
                        #  Diagonal move SE
                        tail_segment["x"] += 1
                        tail_segment["y"] -= 1

                    elif (
                        previous_segment["y"] > tail_segment["y"]
                        and previous_segment["x"] < tail_segment["x"]
                    ):
                        #  Diagonal move NW
                        tail_segment["x"] -= 1
                        tail_segment["y"] += 1

                    elif (
                        previous_segment["y"] < tail_segment["y"]
                        and previous_segment["x"] < tail_segment["x"]
                    ):
                        #  Diagonal move SW
                        tail_segment["x"] -= 1
                        tail_segment["y"] -= 1
            previous_segment = tail_segment

        # print(f"\t{self.positions()}")
        self.tail_positions.append(f"{self.tail[-1]['x']},{self.tail[-1]['y']}")


mover = Mover(1)
for direction, distance in [move.split(" ") for move in moves]:
    # print(f"{direction} {distance} with head starting at {mover.head['x']},{mover.head['y']}")
    distance = int(distance)
    for step in range(distance):
        mover.move_head(direction)
        mover.move_tail()


num_positions = len(set(mover.tail_positions))
print(f"The tail with 1 segment moved into {num_positions} distinct positions.")


mover = Mover(9)
for direction, distance in [move.split(" ") for move in moves]:
    # print(f"{direction} {distance} with head starting at {mover.head['x']},{mover.head['y']}")
    distance = int(distance)
    for step in range(distance):
        mover.move_head(direction)
        mover.move_tail()


num_positions = len(set(mover.tail_positions))
print(f"The tail with 9 segments moved into {num_positions} distinct positions.")
