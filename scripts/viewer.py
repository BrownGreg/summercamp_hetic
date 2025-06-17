import json
import sys
from pathlib import Path

def view_genre(name):
    path = Path("genres") / f"{name.lower()}.json"
    if not path.exists():
        print(f"❌ Genre '{name}' introuvable.")
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"🎧 Genre : {data['genre']}")
    print(f"📍 Origine : {data['origine']}")
    print(f"🎤 Artistes : {', '.join(data['artistes'])}")
    print("🎵 Playlists :")
    for platform, url in data["playlists"].items():
        print(f"  - {platform} : {url}")
    print(f"🌀 Variantes : {', '.join(data['variantes'])}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python viewer.py [genre]")
    else:
        view_genre(sys.argv[1])