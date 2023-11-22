import requests
import json

# CRUD Operations

# C
def post_data():
    URL="http://127.0.0.1:8000/stu_api/"
    data={
        'name':'John',
        'roll':202,
        'city':'Hogworts'
    }

    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# R
def get_data(id=None):
    URL="http://127.0.0.1:8000/stu_api/"
    data ={}
    if id is not None:
        data= {'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)

    data=r.json()
    print(data)

# U
def update_data():
    URL="http://127.0.0.1:8000/stu_api/"
    data={
        'id':2,
        'name':'Stifin',
        'roll':100,
        'city':'USA'
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}

    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# D
def delete_data():
    URL="http://127.0.0.1:8000/stu_api/"
    data={
        'id':2,
    }

    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}

    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)


    # ______functions call_______

# Deserialize_data()
# post_data()
# get_data()
# update_data()
delete_data()