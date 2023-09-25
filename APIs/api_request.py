# api requests

import requests

post_codes_req = requests.get("https://www.bbc.co.uk/news")

print(post_codes_req) # 200 refers to the response code , only asking for the response code
print(post_codes_req.headers) # gives the headers
print(post_codes_req.content) # gives json body as bytes
print(post_codes_req.json()) # short way