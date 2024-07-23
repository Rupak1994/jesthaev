import requests
import json

base_url= "https://reqres.in/api"
aut_token= "token value"

def get_request(page):
    url= f"{base_url}/users?page={page}"
    print("get user:"+ url)
    header={"authorization":aut_token} if aut_token else {}
    response= requests.get(url, headers=header)
    assert response.status_code==200
    json_data=response.json()
    json_str= json.dumps(json_data,indent=4)
    print(f"json get response body{page}:",json_str)
    print("get user done")
    print("=========")

get_request(1)
