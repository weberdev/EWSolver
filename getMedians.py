import csv
import statistics


# File to analyze
FILENAME = "first_printings_trimmed_scraped_types.csv"

# Lists to hold numeric values
mana_values = []
years = []
rarities = []

with open(FILENAME, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        try:
            mana = float(row["mana_value"])
            year = int(row["year"])
            rarity = int(row["rarity"])
        except ValueError:
            continue  # Skip rows with missing or malformed numbers

        mana_values.append(mana)
        years.append(year)
        rarities.append(rarity)

# Compute medians
median_mana = statistics.median(mana_values)
median_year = statistics.median(years)
median_rarity = statistics.median(rarities)

print(f"Median mana value: {median_mana}")
print(f"Median release year: {median_year}")
print(f"Median rarity: {median_rarity} (1=common, 2=uncommon, 3=rare, 4=mythic)")
