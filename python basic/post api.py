import requests
import json

base_url= "https://reqres.in/api"
aut_token= "token value"

def post_request():
    url= base_url+"/users/"
    print("post url:",url)
    headers={"authorization":aut_token}
    data={
        "name":"thapa",
        "email":"manu.com",
        "job":"qa"
    }
    response=requests.post(url, json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post data:",json_str)
    user_id= json_data["id"]
    print("user id",user_id)
    assert response.status_code==201
    assert "name" in json_data
    print("user/post created")
    return user_id
post_request()
