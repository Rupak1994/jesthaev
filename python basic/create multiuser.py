import requests
import json

base_url= "https://reqres.in/api"
aut_token= "token value"
def post_request(user_name):
    url= base_url+ "/users"
    print("post url", url)
    headers={"authorization":aut_token}
    user_ids= []

    for name in user_name:
        data={
            "name":name,
            "job":"qa"
        }
        response = requests.post(url, json=data, headers=headers)
        json_data= response.json()
        json_str= json.dumps(json_data,indent=4)
        print("json data post request:",name,":",json_str)
        user_id= json_data.get("id")
        if user_id:
            user_ids.append(user_id)
        assert response.status_code== 201
        assert "name" in json_data
        print("......post/user is created sucessfully",name,"....")
    return user_ids
for i in range(10):
    user_name=["ram","hari","geeta","sita","shyam","muna"]
    user_ids= post_request(user_name)
    print("created user id", user_ids)


