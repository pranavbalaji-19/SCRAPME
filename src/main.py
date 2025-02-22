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
                check_network_failures()
            elif choice == 2:
                resolve_issues()
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
            elif choice == 2:
                break
            else:
                print("Invalid choice. Please try again.")

main()