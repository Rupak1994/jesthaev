import requests
import json
import string
import random

base_url= "https://reqres.in/api"
aut_token= "token value"
def generate_random_email():
    domain="test.com"
    email_length=8
    random_string=''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email = random_string+ "@" + domain
    return email

def put_request(user_id):
    url = f"{base_url}/users/{user_id}"
    print("get user:" + url)
    header = {"authorization": aut_token}
    data={
        "name":"thapa",
        "email":generate_random_email(),
        "ph":"34444",
        "job":"qa"
    }
    response=requests.put(url, json=data,headers=header)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post data:",json_str)
    assert response.status_code==200
    print("user/put created or update successfully")
put_request(15)
