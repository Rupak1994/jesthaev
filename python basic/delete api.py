import requests
import json


base_url= "https://reqres.in/api"
aut_token= "token value"

def delete_request(user_id):
    url = f"{base_url}/users/{user_id}"
    print("get user:" + url)
    header = {"authorization": aut_token}
    response=requests.delete(url, headers=header)
    assert response.status_code==204
    print("user delete successfully")
delete_request(15)
