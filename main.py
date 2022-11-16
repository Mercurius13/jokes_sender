from trycourier import Courier
import random
import json

client = Courier(auth_token="NoNeOfYoUrBuSiNeSs")

with open("text_files/jokes.json", "r", encoding="utf-8") as f:
    jokes_json = json.load(f)


def query_data_and_send_emails(data):
    data = jokes_json[random.randint(1, 387)]

    resp = client.send_message(
        message={
            "brand_id": "N70YE374RY4TTXH1J7K6NRXH39GT",
            "template": "W3ZPE5X6F6MVP4M9N6WSKD22JYAN   ",
            "to": {
                "email": "meet.siddhant@gmail.com",
            },
            "data": {
                "recipientName": "Siddhant Mohile",
                "joke": f"{data['setup']} {data['punchline']}",
            },
        }
    )
    print(resp)


query_data_and_send_emails(data=jokes_json)
