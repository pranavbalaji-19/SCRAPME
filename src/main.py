from dbsetup import get_connection
from getpass import getpass
from features import *

db, cur = get_connection()

def main():
    while True:
        db, cur = get_connection()
        print("""

        --------------------------------
        ||    Welcome to SCRAP-ME     ||
        --------------------------------
            
        """)
        if input("Proceed with login? (y/n): ").lower() in ("y", "yes"):
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            role = check_and_validate_user(username, password)
            if role in ("admin", "customer"):
                print(f"Welcome {username}!")
            else:
                print(role)
                continue
            
            while True:
                db.commit()
                if role == "admin":
                    print("""
                    
                    1. Check network failures.
                    2. Resolve network issues.
                    3. Resolve customer issues.
                    4. Add new user.
                    5. Check logs.
                    6. Exit.

                    """)
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        latency = float(input("\nEnter latency: "))
                        packet_loss = float(input("Enter packet loss: "))
                        signal_strength = float(input("Enter signal strength: "))
                        check_network_failures(latency, packet_loss, signal_strength)
                    elif choice == 2:
                        details = input("Enter the details: ")
                        resolve_network_issues(details)
                    elif choice == 3:
                        details = input("Enter the details: ")
                        resolve_customer_issues(details)
                    elif choice == 4:
                        new_username = input("\nEnter new username: ")
                        new_password = getpass("Enter new password: ")
                        re_password = getpass("Re-enter new password: ")
                        if new_password != re_password:
                            print("Passwords do not match. Please try again.")
                            continue
                        new_role = input("Enter new role: ")
                        add_user(new_username, new_password, new_role)
                    elif choice == 5:
                        check_logs()
                    elif choice == 6:
                        break
                    else:
                        print("Invalid choice. Please try again.")

                elif role == "customer":
                    print("""
                    
                    1. Raise a complaint.
                    2. Check complaint status.
                    3. Exit.

                    """)
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        complaint = input("Enter your complaint: ")
                        add_customer_complaints(username, complaint)
                    elif choice == 2:
                        cid = int(input("Enter your complaint id: "))
                        check_complaint_status(cid)
                    elif choice == 3:
                        break
                    else:
                        print("Invalid choice. Please try again.")
            
        else:
            break

main()