from dbsetup import get_connection
from getpass import getpass
from features import *

db, cur = get_connection()

def main():
    print("""

    --------------------------------
    ||    Welcome to SCRAP-ME     ||
    --------------------------------
          
    LOGIN TO THE SYSTEM

    """)
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    role = check_and_validate_user(username, password)
    if role in ("admin", "customer"):
        print(f"Welcome {username}!")
    else:
        print(role)
        return
    
    while True:
        if role == "admin":
            print("""
            
            1. Check network failures.
            2. Resolve issues.
            3. Exit.

            """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                latency = float(input("Enter latency: "))
                packet_loss = float(input("Enter packet loss: "))
                signal_strength = float(input("Enter signal strength: "))
                check_network_failures(latency, packet_loss, signal_strength)
                save_changes()
            elif choice == 2:
                type = input("Enter the type of issue: ")
                details = input("Enter the details of the issue: ")
                resolve_issues(type, details)
                save_changes()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")

        elif role == "customer":
            print("""
            
            1. Raise a complaint.
            2. Exit.

            """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                complaint = input("Enter your complaint: ")
                check_customer_complaints(complaint)
                save_changes()
            elif choice == 2:
                break
            else:
                print("Invalid choice. Please try again.")
    
    save_changes()
    close_connection()

main()