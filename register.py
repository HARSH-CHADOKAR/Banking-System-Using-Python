from customer import *
from banking_database import *
import random
from bank import*

def signup():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}'")
    if temp:
        print("Username Already Exists")
        signup()
    else:
        print("Username is Available Please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number = int(random.randint(00000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()

def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Password: ")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("Sign IN Succesfully")
                return username
            else:
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()