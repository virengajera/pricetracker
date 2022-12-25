import re
import db_operations

def isValidLink(link):


    if (link[:22] == "https://www.amazon.de/"):
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
    r_data = db_operations.read_db()
    if r_data.get(email) == None:
        return False
    else:
        return True


def isTrackerExists(email, tracker_name):
    r_data = db_operations.read_db()
    if r_data[email].get(tracker_name) == None:
        return False
    else:
        print("Tracker exists")
        return True