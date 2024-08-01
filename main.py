import requests
from send_email import send_email

topic = "tesla"

api_key = "2495570db3b54f91a827cd6bc3f27eb8"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-07-01&"
       "sortBy=publishedAt&"
       "apiKey=2495570db3b54f91a827cd6bc3f27eb8&"
       "language=en")

request = requests.get(url)
content = request.json()

body = "Subject: Today's news" + "\n"
for article in content["articles"][:5]:
    if article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")

send_email(message=body)



