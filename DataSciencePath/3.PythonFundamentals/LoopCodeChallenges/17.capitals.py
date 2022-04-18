capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]


combined = zip(capitals, countries)


locations = [f"{capital}, {country}" for (capital, country) in combined]

print(locations)
