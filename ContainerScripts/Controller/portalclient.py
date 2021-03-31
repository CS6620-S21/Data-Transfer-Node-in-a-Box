import requests
import json


def login(url, userName, userPassword):
    session = requests.Session()

    response = session.get(url + "?username=" + userName + "&password=" + userPassword)
    print("Login Response : ", response.text)
    return session


def post_register_container(url, session, access_key, secret_key):
    json_object = {
        "access_key": access_key,
        "secret_key": secret_key,
        "port": "9000",
        "ip_address": "localhoast:8000"
    }

    header = {"Content-type": "application/x-www-form-urlencoded"}
    response = session.post(url, data=json_object, headers=header)
    print("Register Response : ", response)
    # print(response.text)


def get_commands(url, session):
    respose = session.get(url)
    print("Get command response : ", respose)
    if respose != None:
        commands = respose.json()
        print("Get command JSON data : ", commands)
        return commands
    return {}
