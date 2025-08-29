import requests
from pathlib import Path
import json

# Hent en tilfeldig vits (med timeout)
resp = requests.get(
    'https://official-joke-api.appspot.com/random_joke', timeout=10)
data = resp.json()

# Skriv ut intro og vitsens setup
print("Her kommer en tilfeldig vits!")
setup = data['setup']
print(setup)

input("Trykk enter for svaret...")

# Skriv ut punchline
punchline = data['punchline']
print(punchline)

# Spør brukeren om vurdering
# f. eks. hahaha
rating = input("Hva synes du om vitsen? Skriv latteren din: ")
laughter = len(rating)
print("Du syns vitsen var", laughter, "/ 10")

# Lagre vitsen i en JSON-fil
SAVE_FILENAME = "joke.json"
with Path(SAVE_FILENAME).open('w', encoding='utf-8') as file:
    json.dump(data, file)
