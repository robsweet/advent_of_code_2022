#!python
from pathlib import Path
import ipdb
import json

payload = Path("input_6.txt").read_text()

for i in range(len(payload) - 1):
    chunk = sorted(list(payload[i : i + 4]))
    if chunk == sorted(list(set(chunk))):
        print(f"Found start of packet at {i + 4}")
        break


for i in range(len(payload) - 1):
    chunk = sorted(list(payload[i : i + 14]))
    if chunk == sorted(list(set(chunk))):
        print(f"Found start of message at {i + 14}")
        break
