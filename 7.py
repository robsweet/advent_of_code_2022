#!python
from pathlib import Path
import ipdb
import json


class DirStruct:
    def __init__(self):
        self.pwd = []
        self.dir_struct = {}
        self.pointer = self.dir_struct
        self.dir_sizes = {}

    def change_dir(self, dir):

        if dir == "/":
            self.pwd = []
        elif dir == "..":
            self.pwd.pop()
        else:
            self.pwd.append(dir)

        self.pointer = self.dir_struct
        for pwd_dir in self.pwd:
            self.pointer = self.pointer[pwd_dir]

    def add_dir(self, dirname):
        self.pointer[dirname] = {}

    def add_file(self, filename, size):
        self.pointer[filename] = size

    def calculate_dir_sizes(self, my_dir, dir_string):
        my_size = 0
        for name, val in my_dir.items():
            if isinstance(my_dir[name], dict):
                my_size += self.calculate_dir_sizes(my_dir[name], f"{dir_string}/{name}")
            else:
                my_size += int(val)

        self.dir_sizes[dir_string] = my_size
        return my_size


lines = Path("input_7.txt").read_text().strip().split("\n")


my_dir = DirStruct()
for line in lines:
    # print(line)
    if line.startswith("$ "):
        if line.startswith("$ cd "):
            my_dir.change_dir(line.replace("$ cd ", ""))
    else:
        if line.startswith("dir "):
            my_dir.add_dir(line.replace("dir ", ""))
        else:
            filesize, filename = line.split()
            my_dir.add_file(filename, filesize)


my_dir.calculate_dir_sizes(my_dir.dir_struct, "")

smalls_sum = 0
for dir_size in my_dir.dir_sizes.values():
    if dir_size <= 100000:
        smalls_sum += dir_size

print(f"Sum of the small directories is {smalls_sum}")

TARGET_FREE = 30_000_000
TOTAL_SPACE = 70_000_000
42_476_859
currently_free = TOTAL_SPACE - my_dir.dir_sizes[""]
space_needed = TARGET_FREE - currently_free

for dir_size in sorted(my_dir.dir_sizes.values()):
    if dir_size > space_needed:
        value = {i for i in my_dir.dir_sizes.keys() if my_dir.dir_sizes[i] == dir_size}
        print(f"Delete dir with size {dir_size} {value}")
        break
