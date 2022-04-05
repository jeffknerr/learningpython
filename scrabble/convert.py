"""
convert json file to plain text, one word per line
"""

import json

fn = "7-letter-words.json"
with open(fn) as f:
    json_data = json.load(f)
#print(json_data)

of = open("words.txt", "w")
for d in json_data:
    of.write(d["word"]+"\n")
of.close()
