import time
import requests
SUBSCRIBE_ENDPOINT = "https://co8wv8tmgg.execute-api.ap-northeast-1.amazonaws.com/subscribe"
UNSUBSCRIBE_ENDPOINT = "https://fzudrg6025.execute-api.ap-northeast-1.amazonaws.com/unsubscribe"


def get_sub_email():
    print("Enter your email.")
    email = input()

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

    response = requests.post(UNSUBSCRIBE_ENDPOINT, json={'email': email})
    if response.status_code != 200:
        print("Something went wrong.")

    print("#######################################################")
    print(response.content.decode())
    print("#######################################################")
