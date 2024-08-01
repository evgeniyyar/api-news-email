import requests
from send_email import send_email


api_key = "2495570db3b54f91a827cd6bc3f27eb8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-01&sortBy=publishedAt&apiKey=2495570db3b54f91a827cd6bc3f27eb8"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 3*"\n"

body = body.encode("utf-8")

send_email(message=body)



