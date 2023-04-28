import httpx
import json
import pandas as pd


# get the response from the api
def get_data(x):
    url = "https://thehub.io/api/companies?includeSuggestions=true&countryCodes[]=SE&page={x}"
    response = httpx.get(url)
    data = response.json()
    return data


# Save the json response as a json file
def save_json(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def main():
    data = get_data(1)
    save_json(data)
    # create a dataframe from the json file:
    df = pd.read_json("data.json")
    df.to_csv("data.csv")


# df = pd.DataFrame(data)
# df.to_csv("data.csv")

if __name__ == "__main__":
    main()

# Path: webscr/data/get_data.py
