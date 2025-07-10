import json
import csv
from collections import defaultdict
from datetime import datetime

with open("allcardscurrent.json","r",encoding="utf-8") as f:
    cards = json.load(f)
    
