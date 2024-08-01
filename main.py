import requests

api_key = "2495570db3b54f91a827cd6bc3f27eb8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-01&sortBy=publishedAt&apiKey=2495570db3b54f91a827cd6bc3f27eb8"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])







