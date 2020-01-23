cities = {"city":"Москва", "temperature":20}

print(cities["city"])
cities["temperature"]-=5

print(cities)

if not cities.get("country"):
    print("key 'contry' not found")

print(cities.get("country", "Россия"))

cities["date"] = '27.05.2019'
print(len(cities))
print(cities)
