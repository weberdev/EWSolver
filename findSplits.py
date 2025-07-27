import csv

# === Load Data ===
cards = []
set_release_order = {'LEA': 1, 'LEB': 2, 'ARN': 3, 'ATQ': 4, 'LEG': 5, 'DRK': 6, 'FEM': 7, 'ICE': 8, 'HML': 9,
                     'ALL': 10, 'MIR': 11, 'MGB': 12, 'VIS': 13, 'POR': 14, 'WTH': 15, 'TMP': 16, 'STH': 17, 'EXO': 18,
                     'P02': 19, 'USG': 20, 'ULG': 21, 'PTK': 22, 'UDS': 23, 'S99': 24, 'MMQ': 25, 'NEM': 26, 'PCY': 27,
                     'INV': 28, 'PLS': 29, 'APC': 30, 'ODY': 31, 'TOR': 32, 'JUD': 33, 'ONS': 34, 'LGN': 35, 'SCG': 36,
                     '8ED': 37, 'MRD': 38, 'DST': 39, '5DN': 40, 'CHK': 41, 'BOK': 42, 'SOK': 43, 'RAV': 44, 'GPT': 45,
                     'DIS': 46, 'CSP': 47, 'TSP': 48, 'TSB': 49, 'PLC': 50, 'FUT': 51, 'LRW': 52, 'MOR': 53, 'SHM': 54,
                     'EVE': 55, 'DRB': 56, 'ALA': 57, 'CON': 58, 'ARB': 59, 'M10': 60, 'HOP': 61, 'ZEN': 62, 'WWK': 63,
                     'ROE': 64, 'ARC': 65, 'M11': 66, 'V10': 67, 'DDF': 68, 'SOM': 69, 'MBS': 70, 'NPH': 71, 'CMD': 72,
                     'M12': 73, 'V11': 74, 'ISD': 75, 'DKA': 76, 'AVR': 77, 'PC2': 78, 'M13': 79, 'DDJ': 80, 'RTR': 81,
                     'GTC': 82, 'DGM': 83, 'M14': 84, 'DDL': 85, 'THS': 86, 'C13': 87, 'BNG': 88, 'JOU': 89, 'CNS': 90,
                     'M15': 91, 'DDN': 92, 'KTK': 93, 'C14': 94, 'FRF': 95, 'DTK': 96, 'ORI': 97, 'CP3': 98, 'DDP': 99,
                     'BFZ': 100, 'EXP': 101, 'C15': 102, 'OGW': 103, 'DDQ': 104, 'SOI': 105, 'EMA': 106, 'EMN': 107,
                     'CN2': 108, 'KLD': 109, 'MPS': 110, 'C16': 111, 'AER': 112, 'AKH': 113, 'MP2': 114, 'HOU': 115,
                     'C17': 116, 'XLN': 117, 'RIX': 118, 'DOM': 119, 'BBD': 120, 'GS1': 121, 'M19': 122, 'C18': 123,
                     'GRN': 124, 'MED': 125, 'G18': 126, 'GNT': 127, 'RNA': 128, 'WAR': 129, 'MH1': 130, 'M20': 131,
                     'C19': 132, 'ELD': 133, 'GN2': 134, 'SLD': 135, 'THB': 136, 'C20': 137, 'IKO': 138, 'M21': 139,
                     'JMP': 140, 'ZNR': 141, 'ZNC': 142, 'MZNR': 143, 'PLST': 144, 'CMR': 145, 'KHM': 146, 'KHC': 147,
                     'MKHM': 148, 'STA': 149, 'STX': 150, 'C21': 151, 'MSTX': 152, 'MH2': 153, 'MMH2': 154, 'AFR': 155,
                     'AFC': 156, 'MAFR': 157, 'MID': 158, 'MIC': 159, 'MMID': 160, 'VOW': 161, 'VOC': 162, 'MVOW': 163,
                     'CC2': 164, 'NEC': 165, 'NEO': 166, 'MNEO': 167, 'Q07': 168, 'SNC': 169, 'NCC': 170, 'MSNC': 171,
                     'CLB': 172, 'MCLB': 173, '2X2': 174, 'DMU': 175, 'DMC': 176, 'MDMU': 177, '40K': 178, 'GN3': 179,
                     'BRO': 180, 'BOT': 181, 'BRC': 182, 'MBRO': 183, 'J22': 184, 'ONE': 185, 'ONC': 186, 'MOM': 187,
                     'MOC': 188, 'MAT': 189, 'LTR': 190, 'LTC': 191, 'CMM': 192, 'WOE': 193, 'WOC': 194, 'WHO': 195,
                     'LCI': 196, 'LCC': 197, 'REX': 198, 'MKM': 199, 'MKC': 200, 'CLU': 201, 'PIP': 202, 'OTJ': 203,
                     'BIG': 204, 'OTC': 205, 'MH3': 206, 'M3C': 207, 'ACR': 208, 'MACR': 209, 'MB2': 210, 'BLB': 211,
                     'BLC': 212, 'DSK': 213, 'DSC': 214, 'FDN': 215, 'J25': 216, 'DFT': 217, 'DRC': 218, 'TDM': 219,
                     'TDC': 220, 'FIN': 221, 'FIC': 222, 'SPE': 223}

# todo: sort sets by release date within year
# do I?
# structuring plan: sets are grouped by year, and sorted within year by release date
# Cards are sorted by color within sets, and within color groupings sorted by mana value
# this allows splits on color, on year, and on mv, with compute time on type being more challenging
# I'll implement this thursday.
# it's wednesday today. need to check for a Python version of LINQ.
# it is actually wednesday, my dudes
# athursdaday come and gone
# Useful notes:
# at time of writing (July 25/25, EOE full spoiler revealed, SPM begins), there are 30255 unique magic cards in the domain of cards in Enchant Worldle.
# Here is the scryfall query I use:
# https://scryfall.com/search?as=grid&order=released&q=%28game%3Apaper%29+is%3Afirstprint&unique=cards

# 25% point: 2021, VOW
# midpoint for unique cards in history: 2015, BFZ
# 75% point: 2005, SOK

#todo: make an array year on year

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
