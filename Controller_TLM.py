import View_TLM,Model_TLM

def main_methods():

  """Enter 1- Log in as Librarian/Admin \nEnter 2- Log in as User/Member \nEnter 0- Close Application"""
  choice = None
  while choice != 0:
    choice = View_TLM.main_menu()
    if choice==1:
        while choice != 0:
            choice = View_TLM.librarian_menu()
            if choice == 1:
                Model_TLM.add_user()
            if choice == 2:
                Model_TLM.add_book()
            if choice==3:
                Model_TLM.update_user()
            if choice == 4:
                Model_TLM.update_bookdetails()
            if choice == 5:
                Model_TLM.delete_user()
            if choice == 6:
                 Model_TLM.delete_book()        
            if choice == 7:
                Model_TLM.books_details()
            if choice == 8:
                 Model_TLM.books_available()
            if choice==9:
                Model_TLM.fine_calc()
            if choice == 10:
                Model_TLM.add_librarian()
            if choice==0:
                break
    if choice==2:
        while choice != 0:
            choice = View_TLM.user_menu()
            if choice == 1:
                Model_TLM.add_user()
            if choice == 2:
                Model_TLM.update_user()
            if choice==3:
                Model_TLM.delete_user()
            if choice == 4:
                Model_TLM.books_details()
            if choice == 5:
                Model_TLM.books_available()
            if choice == 6:
                Model_TLM.fine_calc()        
            if choice == 7:
                Model_TLM.rent_book()
            if choice == 8:
                Model_TLM.return_book()
            if choice == 9:
                email, phone=View_TLM.user_signin()
                if Model_TLM.user_signin(email,phone):
                    print("\nLogin Successful as User!\n")
                else:
                    print("\nLogin Unsuccessful - Invalid Credentials. Please try again!")
                    break
            if choice==0:
                break
           
if __name__ == "__main__":

  main_methods()
    
        