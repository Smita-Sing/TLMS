def main_menu():
    print(' \nWELCOME TO TERMINAL LIBRARY MANAGEMENT SYSTEM (TLM)\n ')
    print('-------------L I B R A R Y    M E N U---------------\n')
    print("Enter 1- Log in as Librarian/Admin \nEnter 2- Log in as User/Member \nEnter 0- Close Application")
    while True: 
        choice=int(input("Please Enter Your Option-->"))
        if choice<=2:
            break
        else:
            print("Invalid Entry By You...Please Try Again!")
    return choice 

def librarian_menu():
    print('\n--------------L I B R A R I A N    M E N U---------------\n')
    print("Enter 1- Add User \nEnter 2- Add Books \nEnter 3- Update User Details"
    "\nEnter 4- Update Book Details \nEnter 5- Delete User \nEnter 6- Delete Books"
    "\nEnter 7- Books Details \nEnter 8- List of Books Available \nEnter 9- Fine Amount" 
    "\nEnter 10- Add Librarian \nEnter 0- Close Application")
    while True: 
        choice=int(input("Please Enter Your Option-->"))
        if choice<=10:
            break
        else:
            print("Invalid Entry By You...Please Try Again!")
    return choice
  
def user_menu():
    print('\n---------------U S E R    M E N U---------------\n')
    print("Enter 1- Register/Add User \nEnter 2- Update User Details \nEnter 3- Delete User"
    "\nEnter 4- Books Details \nEnter 5- List of Books Available \nEnter 6- Fine Amount"
    "\nEnter 7- Rental Operations- Issue/Checkout Book \nEnter 8- Return Book \nEnter 9- Sign in \nEnter 0- Close Application")
    while True:
        choice=int(input("Please Enter Your Option-->"))
        if choice<=9:
            break
        else:
            print("Invalid Entry By You...Please Try Again!")
    return choice

def user_signin():
    email = input("Please Enter Your User Name(Email)-->")
    phone = input("Please Enter Your Contact Number-->")
    return email, phone   
