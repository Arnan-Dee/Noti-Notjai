import time
import requests


def get_sub_email():
    print("Enter your email.")
    email = input()
    SUBSCRIBE_ENDPOINT = "https://eyxqvtbdme.execute-api.ap-northeast-1.amazonaws.com/default/subscribeAnEmail"

    response = requests.post(SUBSCRIBE_ENDPOINT, json={'email': email})
    if response.status_code != 200:
        print("Something went wrong.")
    else:
        print("#######################################################")
        print(response.content.decode())
        print("#######################################################")


def get_unsub_email():
    print("Enter your email.")
    email = input()
    UNSUBSCRIBE_ENDPOINT = "https://s3rwc4hti3.execute-api.ap-northeast-1.amazonaws.com/unsubscribe"

    response = requests.post(UNSUBSCRIBE_ENDPOINT, json={'email': email})
    if response.status_code != 200:
        print("Something went wrong.")

    print("#######################################################")
    print(response.content.decode())
    print("#######################################################")
