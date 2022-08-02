import json
from os import write
from cipher import clean_text
quotes = []

with open("cleaned.json", 'r') as infile:
    data = json.load(infile)
    most = 0
    for quote in data:
        length = len(quote['quoteText'])
        if length <= 100:
            quotes.append(quote)
    
with open("final.json", 'w') as outfile:
    json.dump(quotes, outfile)