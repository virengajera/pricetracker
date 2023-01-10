import tracker_operations
import sys

def main():
    while True:
        message1 = """
        Please Select option:
            1. Add Tracker
            2. View Trackers
            3. Remove Tracker
            4. View Price Only
            5. Exit
        """
        print(message1)

        ch = int(input("Enter Choice : ").strip())

        if ch == 1:

            email = input("Enter Email  :  ").strip().lower()
            tracker_name = input("Enter Tracker Name  :  ").strip().lower()
            link = input("Enter Link  :  ").strip()
            threshold_value = int(input("Enter Threshold Value  :  ").strip())
            tracker_operations.add_tracker(email, tracker_name, link, threshold_value)

        elif ch == 2:

            email = input("Enter Email  :  ").strip().lower()
            tracker_operations.view_tracker(email)

        elif ch == 3:
            
            email = input("Enter Email  :  ").strip().lower()
            tracker_name = input("Enter Tracker Name  :  ").strip().lower()
            tracker_operations.remove_tracker(email,tracker_name)
            
        elif ch == 4:
            print("View Price Only")
            link = input("Enter link here : ").strip().lower()
            tracker_operations.view_price(link)

        elif ch == 5:
            break

        else:
            print("Please enter correct choice")


if __name__ == "__main__":
    for args in sys.argv:
        if args == "track":
            tracker_operations.tracker()
            break

    
    main()
