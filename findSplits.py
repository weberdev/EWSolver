import csv

# === Load Data ===
cards = []
set_release_order = {
    "lea": 0, "leb": 1, "2ed": 2, "arn": 3, "atq": 4, "3ed": 5, "leg": 6, "drk": 7,
    "fem": 8, "4ed": 9, "ice": 10, "chr": 11, "hom": 12, "all": 13, "mir": 14,
    "vis": 15, "wth": 16, "tmp": 17, "sth": 18, "exo": 19, "usg": 20, "ulg": 21,
    "uds": 22, "mmq": 23, "nem": 24, "pcy": 25, "inv": 26, "pls": 27, "apc": 28,
    "ody": 29, "tor": 30, "jud": 31, "ons": 32, "lgd": 33, "scg": 34, "mrd": 35,
    "dst": 36, "5dn": 37, "chk": 38, "bok": 39, "sok": 40, "rav": 41, "gpt": 42,
    "dis": 43, "csp": 44, "tsp": 45, "plc": 46, "fut": 47, "lrw": 48, "mor": 49,
    "shm": 50, "eve": 51, "ala": 52, "con": 53, "arb": 54, "m10": 55, "zen": 56,
    "wwk": 57, "roe": 58, "m11": 59, "som": 60, "mbs": 61, "nph": 62, "m12": 63,
    "isd": 64, "dka": 65, "avr": 66, "m13": 67, "rtr": 68, "gtc": 69, "dgm": 70,
    "m14": 71, "ths": 72, "bng": 73, "jou": 74, "m15": 75, "ktk": 76, "frf": 77,
    "dtk": 78, "ori": 79, "bfz": 80, "ogw": 81, "soi": 82, "emn": 83, "kld": 84,
    "aer": 85, "akh": 86, "hou": 87, "xln": 88, "rix": 89, "dom": 90, "grn": 91,
    "rna": 92, "war": 93, "m20": 94, "eld": 95, "thb": 96, "iko": 97, "znr": 98,
    "khm": 99, "stx": 100, "afr": 101, "mid": 102, "vow": 103, "neo": 104,
    "snc": 105, "dmu": 106, "bro": 107, "one": 108, "mom": 109, "woe": 110,
    "lci": 111, "otj": 112, "mkm": 113,
}

with open("first_printings_trimmed_scraped_types.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            cards.append({
                "name": row["name"],
                "mana_value": float(row["mana_value"]),
                "rarity": int(row["rarity"]),
                "year": int(row["year"])
            })
        except ValueError:
            continue  # Skip rows with malformed numbers


# === Utility: Median ===
def median(values):
    values = sorted(values)
    n = len(values)
    return values[n // 2] if n % 2 == 1 else (values[n // 2 - 1] + values[n // 2]) / 2


# === Compute Medians ===
mv_median = median([c["mana_value"] for c in cards])
rarity_median = median([c["rarity"] for c in cards])
year_median = median([c["year"] for c in cards])


# === Split Scoring Function ===
def compute_split_score(card, all_cards):
    mv_split = sum(1 for c in all_cards if c["mana_value"] < card["mana_value"]) / len(all_cards)
    rarity_split = sum(1 for c in all_cards if c["rarity"] < card["rarity"]) / len(all_cards)
    year_split = sum(1 for c in all_cards if c["year"] < card["year"]) / len(all_cards)

    # How evenly this card splits the population across all three metrics
    return abs(mv_split - 0.5) + abs(rarity_split - 0.5) + abs(year_split - 0.5)


# === Find Best Split ===
best_card = None
best_score = float("inf")

for card in cards:
    score = compute_split_score(card, cards)
    if score < best_score:
        best_card = card
        best_score = score

# === Output Result ===
print(f"Best card: {best_card['name']}")
print(f"Mana Value: {best_card['mana_value']}, Rarity: {best_card['rarity']}, Year: {best_card['year']}")
print(f"Split Score: {best_score:.4f}")
