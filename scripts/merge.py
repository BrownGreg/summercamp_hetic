import json
from pathlib import Path

def merge_all():
    genres = []
    for file in Path("genres").glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            genres.append(data)
    with open("catalogue.json", "w", encoding="utf-8") as f:
        json.dump(genres, f, indent=2, ensure_ascii=False)
    print(f"✅ catalogue.json généré avec {len(genres)} genres.")

if __name__ == "__main__":
    merge_all()