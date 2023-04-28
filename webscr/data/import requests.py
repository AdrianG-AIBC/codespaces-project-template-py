import requests

url = "https://thehub.io/api/companies"

querystring = {"includeSuggestions": "true", "countryCodes[]": "SE", "page": "2"}

response = requests.request("GET", url, params=querystring)

print(response.text)
