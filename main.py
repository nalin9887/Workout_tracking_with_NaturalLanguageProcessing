import requests
from datetime import datetime
import os
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
api_id=os.environ["api_id"]
api_key=os.environ["api_key"]

def what_you_did(activity):
    headers={
        "x-app-id":api_id,
        "x-app-key":api_key,
        "x-remote-user-id":"0"
    }
    what_you_did=activity
    user_data={
     "query":what_you_did,
     "gender":"male",
     "weight_kg":62,
     "height_cm":167.64,
     "age":20
    }
    exersice_api="https://trackapi.nutritionix.com/v2/natural/exercise"
    response=requests.post(url=exersice_api,json=user_data,headers=headers)
    response.raise_for_status()
    data=response.json()
    return data
flag=True
count=0
while flag:
    count+=1
    activity=input("Enter what and how much workout you did today : \n")
    data=what_you_did(activity)
    sheet_url='https://api.sheety.co/89bec35b412ec8fc4de4174c43068bd8/workouts/workouts'
    body = {
        'workout': {
            "date":today_date,
            "time":now_time,
            "exercise":data["exercises"][0]["user_input"].title(),
            "duration":data["exercises"][0]["duration_min"],
            "calories":data["exercises"][0]["nf_calories"],
        }
    }

    response = requests.post(url=sheet_url, json=body)
    response.raise_for_status()
    json = response.json()

    print(json["workout"])
    choice=input("Do you want add more data 'yes' or 'no' or press 'delete' to delete last line you entered. \n")
    if choice=="no":
        flag=False
    elif choice=="delete":
        url = f'https://api.sheety.co/89bec35b412ec8fc4de4174c43068bd8/workouts/workouts/{count}'
        response = requests.delete(url)
        count-=1
        if response.status_code == 200:
            print('Object deleted')


