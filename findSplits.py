import csv

# === Load Data ===
cards = []
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
