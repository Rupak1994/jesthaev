import requests
import json

base_url= "https://reqres.in/api"
aut_token= "token value"

def get_request():
    url= f"{base_url}/users"
    print("get user:"+ url)
    header={"authorization":aut_token}
    response= requests.get(url, headers=header)
    assert response.status_code==200
    json_data=response.json()
    json_str= json.dumps(json_data,indent=12)
    print(f"json get response body:",json_str)
    print("get user done")
    print("=========")

get_request()