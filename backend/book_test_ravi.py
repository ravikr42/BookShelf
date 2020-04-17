import requests
from faker import Faker
import random
import json

url = "http://127.0.0.1:5000/books"



headers = {
  'Content-Type': 'application/json'
}




for _ in range(10000):
    fake = Faker()
    books = {}
    books['title'] = fake.bban()
    books['author'] = fake.name()
    books['rating'] = random.Random().randint(1, 5)
    json_text = json.dumps(books)
    response = requests.request("POST", url, headers=headers, data=json_text)
    print(response.status_code)
    print(response.text.encode('utf8'))
