import json

with open ("quest_db.json", "r", encoding="unf-8") as file:
    data = json.load(file)

print (f"Players: {data["players"]}")
