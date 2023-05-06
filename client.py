import functions


def main():
    print("======================================================")
    print("           Welcome to noti-nojai Application          ")
    print("======================================================")

    print("This is noti-nojai application. The notification that you receive repeatedly is the Jai portion notification to heal your body and mind.")
    print("")

    while True:
        print("What would you like to do subscribe or unsubscribe? (sub, unsub)")
        answer = input(">>> ")
        if answer.lower() in ["sub", "subscribe"]:
            functions.get_sub_email()
            break
        elif answer.lower() in ["unsub", "unsubscribe"]:
            functions.get_unsub_email()
            break
        else:
            print("Invalid input. Please enter 'sub' or 'unsub'.")


if __name__ == "__main__":
    main()
