import json
import sys
from pathlib import Path

def search_keyword(keyword):
    found = []
    for file in Path("genres").glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
        content = json.dumps(data, ensure_ascii=False).lower()
        if keyword.lower() in content:
            found.append(data["genre"])
    if not found:
        print(f"Aucun résultat pour : {keyword}")
    else:
        print("Résultats :")
        for genre in found:
            print(f"- 🎶 {genre}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search.py [mot-clé]")
    else:
        search_keyword(sys.argv[1])