import db_operations
import validation
import scrap
import time

def add_tracker(email, tracker_name, link, threshold_value):
    r_data = db_operations.read_db()

    if not (validation.isValidLink(link)):
        print("Invalid URL")
        return

    if not (validation.isValidEmail(email)):
        print("Invalid Email")
        return

    if not (validation.isEmailExists(email)):
        r_data[email] = {}
        db_operations.update_db(r_data)

    if validation.isTrackerExists(email, tracker_name):
        return
    else:
        r_data[email][tracker_name] = []

    r_data[email][tracker_name].append(link)
    r_data[email][tracker_name].append(threshold_value)

    db_operations.update_db(r_data)


def view_tracker(email):
    r_data = db_operations.read_db()
    if not (validation.isValidEmail(email)):
        print("Invalid Email")
        return
    
    if not(validation.isEmailExists(email)):
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
    r_data = db_operations.read_db()

    if not (validation.isValidEmail(email)):
        print("Invalid Email")
        return
    
    if not (validation.isEmailExists(email)):
        print("Email does not exists")
        return

    if not (validation.isTrackerExists(email, tracker_name)):
        print("Tracker Name does not exists")
        return
    
    del r_data[email][tracker_name]

    db_operations.update_db(r_data)

def view_price(link):
    if not (validation.isValidLink(link)):
        print("Invalid Link")
        return
    
    price = scrap.scrapping(link)
    print("Price in EUR is : ", price)

def tracker():
    while True:
        time.sleep(2)
        print("TRACKER IS TRACKING")
        #get data from db
        #Get link
        #already tracked yes or no
        #If yes amazonn hit link
        #if latest price < threshold value : print message Price dropped
        #set flag to already tracked to yes