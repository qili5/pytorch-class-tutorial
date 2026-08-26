import requests

pokemon = "pikachu"

API_URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

response = requests.get(API_URL)

print("Status Code:", response.status_code)

data = response.json()

print("Name:", data["name"])
print("Height:", data["height"])
print("Weight:", data["weight"])

print("Abilities:")
for item in data["abilities"]:
    print("-", item["ability"]["name"])