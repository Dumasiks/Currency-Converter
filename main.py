import requests


def total(s, am):
    print("Checking the cache...")
    if s.lower() in cache.keys():
        print("Oh! It is in the cache!")
        return round(cache.get(s) * am, 2)
    else:
        print("Sorry, but it is not in the cache!")
        return round(requests.get(f"http://www.floatrates.com/daily/{second_currency}.json").json()[currency]["inverseRate"] * am, 2)


cache = dict()
usd_rate = requests.get("http://www.floatrates.com/daily/usd.json").json()
eur_rate = requests.get("http://www.floatrates.com/daily/eur.json").json()
currency = input()
try:
    cache["usd"] = usd_rate[currency]["inverseRate"]
except KeyError:
    pass
try:
    cache["eur"] = eur_rate[currency]["inverseRate"]
except KeyError:
    pass

while True:
    second_currency = input()
    if second_currency == "":
        break
    amount = float(input())
    print(f"You received {total(second_currency, amount)} {second_currency.upper()}.")
    cache[f"{second_currency}"] = requests.get(f"http://www.floatrates.com/daily/{second_currency}.json").json()[currency]["inverseRate"]
