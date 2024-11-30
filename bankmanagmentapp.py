# full bank managing controlling program which only include main 3 options in banks(account balanace, money withdraw, money deposite)

from datetime import date

user_dict = {
    1001: {
        "user_name": "chanuka",
        "current_balance": 0,
        "opened_date": 2024-9-27,
        "account_type": "youth",
        "user_class": ""
    }
}

def check_input_type(a):
    try:
        a = float(a)
    except:
        print("Invalid input!")
    
    return a

class User:
    def __init__(self, account_number, user_name, current_balance, opened_date, account_type): # 3 different account types: child, youth, older
        self.account_number = account_number
        self.user_name = user_name
        self.current_balance = current_balance
        self.opened_date = opened_date
        self.account_type = account_type

    def print_account_balance(self):
        print(f"You Account have ${self.current_balance}")

    def deposite_money(self, depoiste_amount):
        self.current_balance = self.current_balance + depoiste_amount
        print(f"Your have successfully deposite ${depoiste_amount} \nYou Account currently have ${self.current_balance}")

    def withdraw_money(self, requested_amount):
        if self.current_balance < requested_amount:
            print("Insufficient Account balance!")
        elif self.current_balance > requested_amount and self.current_balance < requested_amount+10:
            print(f"Must be saved $10 in your account!\n You can withdraw ${self.current_balance-10}...")
        elif self.current_balance >= requested_amount+10:
            self.current_balance = self.current_balance - requested_amount
            print("Transaction was successfully completed!")

    def __repr__(self):
        return f"Account no:{self.account_number}\n\tAccount name:{self.user_name}\n\tOpened date:{self.opened_date}\n\tAccount type:{self.account_type}"


def account_operations(user_class):
    while True:
        print("Select account options\n\t1.Account balance\n\t2.Money deposite\n\t3.Money withdraw\n\t4.Back to main menu\n\t5.Exit")
        option_type = input("Enter option: ")
        try:
            option_type = int(option_type)
            if option_type not in [1, 2, 3, 4, 5]:
                print("Invalid option. Try again!")
                continue
        except:
            print("Invalid option. Re-enter option!")
            continue
        
        # check balanace
        if option_type == 1:
            user_class.print_account_balance()

        # deposite money
        elif option_type == 2:
            while True:
                depoiste_amount = input("Enter deposite amount: ")
                try: 
                    depoiste_amount = float(depoiste_amount)
                    if depoiste_amount <= 0:
                        print("Invalid amount! Re-enter")
                        continue
                except:
                    print("Invalid amount! Re-enter")
                    continue
                break
            user_class.deposite_money(depoiste_amount)

        # withdraw money
        elif option_type == 3:
            while True:
                withdraw_amount = input("Enter withdraw amount: ")
                try:
                    withdraw_amount = float(withdraw_amount)
                    if withdraw_amount <= 0:
                        print("Invalid amount! Re-enter")
                        continue
                except:
                    print("Invalid amount! Re-enter")
                    continue
                break
            user_class.withdraw_money(withdraw_amount)

        # back to main manu
        elif option_type == 4:
            break

        # exit 
        elif option_type == 5:
            print("End of the program!")
            exit(0)

def main():
    while True:
        # select a main option
        while True:
            print("Select Option\n\t1.Create Account\n\t2.Select Account\n\t3.Exit")
            main_option = input("Enter main option: ")
            
            try:
                main_option = int(main_option)
                if main_option not in [1, 2, 3]:
                    print("Invalid option. re-enter!")
                    continue
            except:
                print("Invalid input. re-enter!")
                continue
            break
        
        # create account
        if main_option == 1:
            account_number = int(input("Enter new account number(It must contain 4 digit code that given by bank): "))
            # want to check if it is avalable or not(account number)
            user_name = input("Enter your full name: ")
            opened_date = date.today()
            account_type = input("Enter your account type(It must be a type among 'child', 'youth' or 'older'): ")

            user_class = User(account_number, user_name, 0, opened_date, account_type)

            user_dict[account_number] = {
                "user_name": user_name,
                "current_balanace": 0,
                "opened_date": opened_date,
                "account_type": account_type,
                "user_class": user_class
            }
            print("\n")
            print(repr(user_dict[account_number]["user_class"]))
            print("Successfully create your bank account!\n")

        # select account
        elif main_option == 2:
            while True:
                selected_account_number = input("Enter Account number : ")
                try:
                    selected_account_number = int(selected_account_number)
                    if selected_account_number not in user_dict:
                        print("Incorrect account number. Please check again!")
                        continue
                except:
                    print("Incorrect account number. Please check again!")
                    continue
                break
            print(f"Welcome back {user_dict[selected_account_number]["user_name"]}!")
            account_operations(user_dict[selected_account_number]["user_class"])

        # exit
        elif main_option == 3:
            print("End of the program!")
            exit(0)


if __name__ == "__main__":
    main()

print("Hello world");