from dotenv import load_dotenv
load_dotenv()
import json
import os
import requests
from collection import collection

DATA_SERVICE_API_KEY = os.environ["DATA_SERVICE_API_KEY"]
DATA_SERVICE_URL = os.environ["DATA_SERVICE_URL"]

def request(offset=0, limit=2000):
    url = f"{DATA_SERVICE_URL}/export?offset={offset}&limit={limit}"
    print(f"{url}\n")
    response = requests.get(url, headers={"x-api-key": DATA_SERVICE_API_KEY})
    data = json.loads(response.text)
    if len(data["records"]):
        records = data["records"]
        records = list(map(lambda a: {**a, "payload": json.loads(a["payload"])}, records))
        ids = list(map(lambda a: a["payload"]["recordId"], records))
        documents = list(map(lambda a: a["searchText"], records))
        collection.add(
            documents=documents,
            ids=ids
        )
        request(offset + 2000, limit)

request()
