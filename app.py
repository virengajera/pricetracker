import json
import re

def read_db():
    json_file = open('db.json','r')
    data = json.load(json_file)
    json_file.close()
    return data


def update_db(data):
    json_file = open('db.json','w')
    json.dump(data,json_file)
    json_file.close()
    return "Data Updated"



def isValidLink(link):
    amz = link[:18]
    if amz == "https://amazon.de/":
        print("Valid amazon url")
        return True
    else:
        return False
    print()

def add_tracker(email,link,threshold_value):
    r_data = read_db()
    if not(isValidLink(link)):
        print("Invalid URL")
    

def view_tracker(email):
    pass

def remove_tracker():
    pass

def view_price():
    link = input("Enter Link Here: ")
    validate(link)
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

        ch = int(input("Enter Choice: "))
        if ch == 1:
            print("Add Tracker f ")
            add_tracker("a","b","c")
        elif ch == 2:
            print("View Tracker fn")
        elif ch == 3:
            print("Remove Tracker fn")
        elif ch == 4:
            print("View Price Only")
            view_price()
        elif ch == 5:
            break
        else:
            print("Please enter correct choice")


if __name__=="__main__":
    main()