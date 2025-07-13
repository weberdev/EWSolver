import csv
import statistics

# === Configuration ===
INPUT_FILE = "first_printings_trimmed_scraped_types.csv"

# === Data Containers ===
mana_values = []
release_years = []
rarities = []

# === Load and Parse CSV ===
with open(INPUT_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        try:
            mana = float(row["mana_value"])
            year = int(row["year"])
            rarity = int(row["rarity"])
        except ValueError:
            continue  # Skip any rows with malformed data

        mana_values.append(mana)
        release_years.append(year)
        rarities.append(rarity)

# === Compute Medians ===
median_mana = statistics.median(mana_values)
median_year = statistics.median(release_years)
median_rarity = statistics.median(rarities)

# === Output Summary ===
print(f"Total cards processed: {len(mana_values)}")
print(f"Median Mana Value:     {median_mana}")
print(f"Median Release Year:   {median_year}")
print(f"Median Rarity:         {median_rarity} (1=Common, 2=Uncommon, 3=Rare, 4=Mythic)")
