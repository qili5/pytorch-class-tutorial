import requests

API_URL = "http://export.arxiv.org/api/query?search_query=all:large language models"

response = requests.get(API_URL)

print(response.status_code)
print(response.text)
