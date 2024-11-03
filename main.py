from yandex_tracker_client import TrackerClient
from datetime import datetime
import pandas as pd
import numpy as np
import requests
from secret_keys import my_token, my_cloud_org_id

client = TrackerClient(token=my_token,
                       cloud_org_id=my_cloud_org_id)

df = pd.read_excel(r'C:\Users\Игорь\PycharmProjects\Tracker_OT\tasks_generator_1.xlsx')


def my_function():
    session = requests.Session()
    url = "https://api.tracker.yandex.net/v2/issues/"
    json = {
        "queue": "TREK",
        "summary": "Test Issue",
        "type": "bug",
        "assignee": "<user_login>"
    }
    head = {
        "Authorization": "OAuth " + my_token,
        "X-Cloud-Org-ID": my_cloud_org_id
    }
    session.headers.update(head)
    response = session.post(url, json=json)
    data = response.json()
    print(response)
    print(data)


# my_function()


for i, row in df.iterrows():
    issue = client.issues.create(
        queue='LRS',
        summary=row['Задача'],
        type={'name': 'Задача'},
        description=row['Описание'],
        assignee=row['Исполнитель']
    )


class Car:
    def __init__(self):
        pass
