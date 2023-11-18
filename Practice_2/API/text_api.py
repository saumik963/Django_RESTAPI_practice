import requests
import json

def Deserialize_data():
    URL="http://127.0.0.1:8000/stu_create/"

    data={
        'name':'Harmoine Gringer',
        'roll':103,
        'city':'Wogwords'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

# CRUD Operations

# C
def post_data():
    URL="http://127.0.0.1:8000/stu_apic/"
    data={
        'name':'Neville',
        'roll':101,
        'city':'Wogwords'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

# R
def get_data(id=None):
    URL="http://127.0.0.1:8000/stu_apic/"
    data ={}
    if id is not None:
        data= {'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)

    data=r.json()
    print(data)

# U
def update_data():
    URL="http://127.0.0.1:8000/stu_apic/"
    data={
        'id':11,
        'name':'Neville Longbottom',
        'roll':102,
        'city':'Wogwarts'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
# D
def delete_data():
    URL="http://127.0.0.1:8000/stu_apic/"
    data={
        'id':10,
    }

    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)


    # ______functions call_______

# Deserialize_data()
# post_data()
# get_data(3)
# update_data()
delete_data()