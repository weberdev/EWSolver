import pandas as pd

# Load the CSV
df = pd.read_csv("first_printings_trimmed_scraped_types.csv")

# Ensure mana_value and rarity are numeric
df['mana_value'] = pd.to_numeric(df['mana_value'], errors='coerce')
df['rarity'] = pd.to_numeric(df['rarity'], errors='coerce')

# Drop rows with NaN values in key columns just to be safe
df = df.dropna(subset=['mana_value', 'rarity'])

# Compute totals
total_mana_value = df['mana_value'].sum()
total_rarity_score = df['rarity'].sum()

# Median values
median_mana_value = df['mana_value'].median()
median_rarity = df['rarity'].median()
median_year = df['year'].median()

# Unique counts
unique_type_combos = df['types'].nunique()
unique_subtype_combos = df['subtypes'].nunique()

# Most common type combos
type_freq = df['types'].value_counts().head(10)
subtype_freq = df['subtypes'].value_counts().head(10)

# Print results
print("=== SUMMARY ===")
print(f"Total Mana Value: {total_mana_value}")
print(f"Total Rarity Score: {total_rarity_score}")
print(f"Median Mana Value: {median_mana_value}")
print(f"Median Rarity: {median_rarity}")
print(f"Median Year: {median_year}")
print(f"Unique Type Combos: {unique_type_combos}")
print(f"Unique Subtype Combos: {unique_subtype_combos}")
print("\n=== Most Common Type Combos ===")
print(type_freq)
print("\n=== Most Common Subtype Combos ===")
print(subtype_freq)
