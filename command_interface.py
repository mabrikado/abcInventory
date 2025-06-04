import Inventory
import getpass


def main():
    print("ABC Inventory Management System")

    #prompt user for choice
    user_input = input("Register or Log in (R/L)").lower()

    #verify user choice
    if user_input not in ["R" , "L"]:
        print("Invalid Choice")
        return
    user_input = input("Enter username :")
    password_input = getpass.getpass("Enter your password: ")

    user = None
    if user_input == "L":
        user = Inventory.User.log_user(user_input , password_input)
        if not user:
            print("Username and password is invalid!!")
            return
    else:
        user = Inventory.User.create_user(user_input , password_input)
        if not user:
            print("Username already exist")
            return

    #Run Inventory operations
    Inventory.main(user)        




if __name__ == "__main__":
    main()