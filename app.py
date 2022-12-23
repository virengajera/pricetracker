import json
import re


def read_db():
    json_file = open('db.json', 'r')
    data = json.load(json_file)
    json_file.close()
    return data


def update_db(data):
    json_file = open('db.json', 'w')
    json.dump(data, json_file)
    json_file.close()
    print("Data Updated")


def isValidLink(link):
    amz = link[:18].lower()
    if amz == "https://amazon.de/":
        print("Valid amazon url")
        return True
    else:
        return False


def isValidEmail(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(email_regex, email)):
        print("Valid Email")
        return True
    else:
        return False


def isEmailExists(email):
    r_data = read_db()
    if r_data.get(email) == None:
        return False
    else:
        return True


def isTrackerExists(email, tracker_name):
    r_data = read_db()
    if r_data[email].get(tracker_name) == None:
        return False
    else:
        print("Tracker Name Already exists")
        return True


def add_tracker(email, tracker_name, link, threshold_value):
    r_data = read_db()

    if not (isValidLink(link)):
        print("Invalid URL")
    if not (isValidEmail(email)):
        print("Invalid Email")

    if not (isEmailExists(email)):
        r_data[email] = {}

    if not (isTrackerExists(email, tracker_name)):
        r_data[email][tracker_name] = []

    r_data[email][tracker_name].append(link)
    r_data[email][tracker_name].append(threshold_value)

    update_db(r_data)


def view_tracker(email):
    r_data = read_db()
    if not (isValidEmail(email)):
        print("Invalid Email")
        return
    
    if not(isEmailExists(email)):
        print("Email does not exists")
        return

    print("********** LIST OF TRACKERS ************")
    print("--------------------------------")
    for k,v in r_data.get(email).items():
        print("Tracker Name : ", k)
        print("Link : ", v[0])
        print("Threshold Values : ", v[1])
        print("--------------------------------")


def remove_tracker(email, tracker_name):
    r_data = read_db()

    if not (isValidEmail(email)):
        print("Invalid Email")
        return
    
    if not (isEmailExists(email)):
        print("Email does not exists")
        return

    if not (isTrackerExists(email, tracker_name)):
        print("Tracker Name does not exists")
        return
    
    del r_data[email][tracker_name]

    update_db(r_data)

def view_price(link):
    link = input("Enter Link Here : ")
    if not (isValidLink(link)):
        print("Invalid Link")
        print()

    print("Here is the price")


def tracker():
    pass


def main():
    while True:
        m1 = """
        Please Select option:
            1. Add Tracker
            2. View Trackers
            3. Remove Tracker
            4. View Price Only
            5. Exit
        """
        print(m1)

        ch = int(input("Enter Choice : ").strip())

        if ch == 1:

            email = input("Enter Email  :  ").strip().lower()
            tracker_name = input("Enter Tracker Name  :  ").strip().lower()
            link = input("Enter Link  :  ").strip()
            threshold_value = int(input("Enter Threshold Value  :  ").strip())
            add_tracker(email, tracker_name, link, threshold_value)

        elif ch == 2:

            email = input("Enter Email  :  ").strip().lower()
            view_tracker(email)

        elif ch == 3:
            
            email = input("Enter Email  :  ").strip().lower()
            tracker_name = input("Enter Tracker Name  :  ").strip().lower()
            remove_tracker(email,tracker_name)
            
        elif ch == 4:
            print("View Price Only")
            view_price(link)
        elif ch == 5:
            break
        else:
            print("Please enter correct choice")


if __name__ == "__main__":
    main()
