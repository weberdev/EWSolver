import json
import csv
from collections import defaultdict
from datetime import datetime

with open("allcardscurrent.json","r",encoding="utf-8") as f:
    cards = json.load(f)

first_printings = {}

for card in cards:
    oracle_id = card.get("oracle_id")
    release_date = card.get("released_at")

    if not oracle_id or not released_at:
        continue
    if oracle_id not in first_printings or released_at < first_printings[oracle_id]["released_at"]:
        first_printings[oracle_id] =card

    
def parse_types(line):
    if "-" in line:
        type_segment, sub_segment = line.split("-",1)
        types = [t.strip() for t in type_segment.strip().split()]
        subtypes = [s.strip() for s in sub_segment.strip().split()]
        else:
            types = [t.strip() for t in type_segment.strip().split()]
            subtypes = []

        return types, subtypes
