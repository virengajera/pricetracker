""" 

1. Add Tracker
2. View Trackers
3. Remove Tracker
4. View Price Only
 """


""" 
 1. Add Tracker
    - Enter Link, Threshold value, email
    - Validate Link
    - Add Tracker
 
"""

def validate():
    pass

def add_tracker(link,threshold_value,email):
    pass

def view_tracker():
    pass

def remove_tracker():
    pass

def view_price():
    pass

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
        elif ch == 2:
            print("View Tracker fn")
        elif ch == 3:
            print("Remove Tracker fn")
        elif ch == 4:
            print("View Price Only")
        elif ch == 5:
            break
        else:
            print("Please enter correct choice")


if __name__=="__main__":
    main()