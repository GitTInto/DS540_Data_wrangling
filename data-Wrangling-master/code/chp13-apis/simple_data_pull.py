import oauth2

API_KEY = 'Q7XSeZS1a06Tu0mzeETrXpD5w'
API_SECRET = '9DuJLEER4puekE9ysdaoXM3zpCu5WtOYXy6IJO8lnW66M54o48'
TOKEN_KEY = '2168705305-bWFKU4PoWHo2X4hAUKViZuVN56c9JvsdOQBhgaO'
TOKEN_SECRET = 'f8wqKpvcwkkNIw6tzDFDEunuJdFeJQmmhgrEo0fKnLmdg'


def oauth_req(url, key, secret, http_method="GET", post_body="",
              http_headers=None):
    consumer = oauth2.Consumer(key=API_KEY, secret=API_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method,
                                   body=post_body, headers=http_headers)
    return content


url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23childlabor'
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)

with open("../../data/chp13/hashchildlabor.json", "w") as data_file:
    data_file.write(data)
