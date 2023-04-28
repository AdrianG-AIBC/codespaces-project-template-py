# Description: Download data from thehub.io api and save to json and csv

import httpx
import pandas as pd
import csv

# from selectolax.parser import HTMLParser
import json
import asyncio


def download_json(url):
    with httpx.Client() as client:
        resp = client.get(url)
        for node in resp.json()["docs"]:
            yield node


def save_to_json(data):
    with open("results.json", "w") as f:
        json.dump(data, f)


def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("results.csv", index=False)


def main():
    results = []
    for i in range(1, 160):
        print("page", i)
        url = f"https://thehub.io/api/companies?includeSuggestions=true&countryCodes[]=SE&page={i}"
        for item in download_json(url):
            results.append(item)
    print(len(results))
    save_to_csv(results)
    save_to_json(results)


if __name__ == "__main__":
    main()
