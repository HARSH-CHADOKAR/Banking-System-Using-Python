from register import *
from bank import *

print("Welcome to Jarvis Banking System")
status = False
while True:
    try:
        print("\n1. Sign UP\n2. Sign In")
        register = input("Choose an option (1 for Sign UP, 2 for Sign In): ")
        
        if register == "1":
            signup()
            print("SignIn to use bank Facitity")
            user = SignIn()
            status = True
            break

        elif register == "2":
             user = SignIn()
             status = True
             break
        else:
            print(" Please enter a valid option (1 or 2).")

    except ValueError:
        print(" Invalid input. Please enter a number (1 or 2).")

account_number = db_query(
    f"SELECT account_number FROM customers WHERE username = '{user}';")

while status:
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                             "2. Cash Deposit\n"
                             "3. Cash Withdraw\n"
                             "4. Fund Transfer\n"
                             "5. Exit\n "
                             ))
        if facility >= 1 and facility <= 5:
            if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceequiry()
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

            elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 4:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number: "))
                        amount = int(input("Enter Money to Transfer: "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            elif facility == 5:
                print("Thanks For Using Banking Services")
                status = False
        else:
            print("Please Enter Valid Input From Options")
            continue

    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue