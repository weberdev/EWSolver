import json
import csv
from collections import defaultdict
from datetime import datetime

with open("allcardscurrent.json","r",encoding="utf-8") as f:
    cards = json.load(f)

NON_PLAYABLE_TYPES = {
    "Plane", "Scheme", "Vanguard", "Conspiracy", "Card"
    "Token", "Emblem", "Attraction", "Dungeon", "Sticker"
}

first_printings = {}

for card in cards:
    oracle_id = card.get("oracle_id")
    released_at = card.get("released_at")

    if not oracle_id or not released_at:
        continue
    if oracle_id not in first_printings or released_at < first_printings[oracle_id]["released_at"]:
        first_printings[oracle_id] =card

    
def parse_types(line):
    if "—" in line:  # Em dash
        type_segment, sub_segment = line.split("—", 1)
        types = [t.strip() for t in type_segment.strip().split()]
        subtypes = [s.strip() for s in sub_segment.strip().split()]
    else:
        types = [t.strip() for t in line.strip().split()]
        subtypes = []
    return types, subtypes


with open("first_printings_trimmed_scraped_types.csv", "w", newline='', encoding="utf-8") as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(["name", "mana_value", "color_identity", "types", "subtypes", "set", "year", "rarity"])
    
    for card in first_printings.values():
        name = card.get("name", "")
        mana_value = card.get("cmc", 0)
        color_identity = ",".join(card.get("color_identity", []))
        type_line = card.get("type_line", "")
        types, subtypes = parse_types(type_line)
        if any(t in NON_PLAYABLE_TYPES for t in types):
            continue
        type_str = ",".join(types)
        subtype_str = ",".join(subtypes)
        set_code = card.get("set", "")
        year = card.get("released_at", "0000")[:4]
        rarity = card.get("rarity", "")
        
        writer.writerow([name, mana_value, color_identity, type_str, subtype_str, set_code, year, rarity])

print("end of run")
