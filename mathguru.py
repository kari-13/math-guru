import json
from typo import flatten_json, match_full, match_level_by_level

json_path = 'Math.json'
with open(json_path, 'r') as file:
    datab = json.load(file)

flat_data = flatten_json(datab)
while True:
    a = input("enter a math theorem to find its explanation (use spaces for nested): ").strip()
    if a.lower() == 'exit':
        print("thank you for using my app :) \n  @kari_13")
        break
    # Try full fuzzy match first
    key, value, score = match_full(a, flat_data)
    if key and not isinstance(value, dict):
        print(value)
        continue
    # If full match fails or value is dict, try level-by-level fuzzy match
    keys = a.split()
    result = match_level_by_level(keys, datab)
    if result and not isinstance(result, dict):
        print(result)
        continue
    # Try direct nested key access
    result = datab
    try:
        for k in keys:
            result = result[k]
        print(result)
    except Exception:
        print("theorem not found")



    
