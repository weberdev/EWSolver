import csv

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
            continue  # skip rows with bad data
def median(lst):
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2

mv_median = median([c["mana_value"] for c in cards])
rarity_median = median([c["rarity"] for c in cards])
year_median = median([c["year"] for c in cards])
def compute_split_score(card, cards, mv_median, rarity_median, year_median):
    mv_split = sum(1 for c in cards if (c["mana_value"] < card["mana_value"])) / len(cards)
    rarity_split = sum(1 for c in cards if (c["rarity"] < card["rarity"])) / len(cards)
    year_split = sum(1 for c in cards if (c["year"] < card["year"])) / len(cards)

    # Score is how far from 0.5 the splits are — lower is better
    score = abs(mv_split - 0.5) + abs(rarity_split - 0.5) + abs(year_split - 0.5)
    return score
best_card = None
best_score = float("inf")

for card in cards:
    score = compute_split_score(card, cards, mv_median, rarity_median, year_median)
    if score < best_score:
        best_score = score
        best_card = card

print(f"Best card: {best_card['name']}")
print(f"Mana Value: {best_card['mana_value']}, Rarity: {best_card['rarity']}, Year: {best_card['year']}")
print(f"Split score: {best_score:.4f}")
