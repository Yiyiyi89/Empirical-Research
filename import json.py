import json
import pandas as pd

file_path = r"C:\Users\17284\Desktop\J_Article Network\openalex-snapshot--sources\updated_date=2024-07-31\part_000\part_000.json"

data = []

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        json_obj = json.loads(line)
        data.append(json_obj)

df = pd.json_normalize(data)

print(json.dumps(data, indent=4, ensure_ascii=False))
