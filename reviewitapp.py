from reviewit import ReviewIT


class ReviewITApp:
    """
    Model for ReviewITApp
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.review_data = ReviewIT()
        self.logged_in_user = self.display_action_sign_in_menu()
        self.display_action_menu()


    def display_sign_in_menu(self) -> None:
        """
        Method that displays sign in menu
        """
        print("-"*150)
        print("ReviewIT")
        print("-"*150)
        print("1. Sign in")
        print("2. Create account")
        print("3. Exit")
        print("-"*150)


    def display_menu(self) -> None:
        """
        Method to display menu
        """
        print("-"*150)
        print("ReviewIT")
        print("-"*150)
        print("1. Display reviews")
        print("2. Search for reviews")
        print("3. Add review")
        print("4. Remove review")
        print("5. Exit")
        print("-"*150)
        

    def display_error_menu(self) -> None:
        """
        Method to display error message
        """
        print("-"*150)
        print("Enter a valid choice!")
        print("-"*150)


    def display_exit_menu(self) -> None:
        """
        Method to display message when leaving application
        """
        print("-"*150)
        print(f"Thanks for today {self.logged_in_user}!")
        print("-"*150)


    def display_create_user(self) -> None:
        """
        Method for creating user account
        """
        #Would be implemented if the application used a SQL or NoSQL database or saved the information from the application after each run
        pass


    def display_reviews(self) -> None:
        """
        Method to display reviews
        """
        reviews = self.review_data.get_review_database()

        if len(reviews) == 0:
            print("-"*150)
            print("There are no reviews!")
            print("-"*150)

        else:
            print("-"*150)
            print("Found the following reviews...")
            print("-"*150)
            
            for review in reviews:
                print(review)
            
            print("-"*150)
            print(f"(Displays {len(reviews)} of total {len(reviews)} reviews on ReviewIT)")
            print("-"*150)


    def display_search_reviews(self) -> None:
        """
        Method to display reviews based on the users search input
        """
        reviews = self.review_data.get_review_database()

        if len(reviews) == 0:
            print("-"*150)
            print("There are no reviews!")
            print("-"*150)


        else:
            search_input = input("Enter search: ")
            results = self.review_data.get_search_review(search_input)

            if len(results) == 0:
                print("-"*150)
                print(f"Could not find any reviews with search input '{search_input}'")
                print("-"*150)
        

            else:
                print("-"*150)
                print(f"Found the following reviews with search input '{search_input}'...")
                print("-"*150)
                
                for review in results:
                    print(review)
                
                print("-"*150)
                print(f"(Displays {len(results)} of total {len(results)} reviews)")
                print("-"*150)


    def display_remove_review(self) -> None:
        """
        Method for removing review
        """
        remove_input = input("Enter product to remove: ")

        if self.review_data.get_remove_review(remove_input):
            print("-"*150)
            print(f"Sucessfully removed review '{remove_input}'")
            print("-"*150)


        else:
            print("-"*150)
            print(f"Could not find review '{remove_input}'")
            print("-"*150)


    def display_add_review(self) -> None:
        """
        Method for adding review
        """
        print("-"*150)
        print("Select one of the following to create a review!")
        print("-"*150)
        print("1. Smartwatch ")
        print("2. Phone")
        print("3. Computer")
        print("-"*150)

        while True:
            try:
    
                user_choice = input("Enter choice: ")
                
                review_username = self.logged_in_user
                product_id = int(input("Enter ID: "))
                product_name = input("Enter name: ")
                product_supplier = input("Enter supplier: ")
                product_price = int(input("Enter price ($): "))
                product_review = input("Write review: ")
                product_grade = int(input("Enter grade (1-10): "))

                if user_choice == "1":

                    try:
                        watch_diameter = int(input("Enter diamenter (mm): "))
                        watch_strap = input("Enter type of strap: ")
                        self.review_data.add_review_smartwatch(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade, watch_diameter, watch_strap)
                        break
                    
                    except:
                        print("-"*150)
                        print("Error! Could not add review")
                        print("-"*150)
                        break


                elif user_choice == "2":

                    try:
                        phone_screensize = int(input("Enter screensize (inch): "))
                        phone_memory = int(input("Enter memory (GB): "))
                        self.review_data.add_review_phone(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade, phone_screensize, phone_memory)
                        break
                    
                    except:
                        print("-"*150)
                        print("Error! Could not add review")
                        print("-"*150)
                        break
                    

                elif user_choice == "3":
                    
                    try:
                        computer_memory = int(input("Enter memory (GB): "))
                        computer_ram =int( input("Enter RAM (GB): "))
                        self.review_data.add_review_computer(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade, computer_memory, computer_ram)
                        break

                    except:
                        print("-"*150)
                        print("Error! Could not add review")
                        print("-"*150)
                        break


                else:
                    print("-"*150)
                    print("Please enter a vaild choice!")
                    print("-"*150)
            
            except:
                print("-"*150)
                print("Error, try enter the right datatype!")
                print("-"*150)
                break


    def display_action_sign_in_menu(self) -> str:
        """
        Method with all methods implemented for signed out users
        """
        
        while True:
            self.display_sign_in_menu()
            menu_choice = input("Enter choice: ")


            if menu_choice == "1":
                logged_in_user = input("Enter username: ")
                return logged_in_user
                break


            elif menu_choice == "2":
                #Add to JSON
                self.display_create_user()


            elif menu_choice == "3":
                print("-"*150)
                print("Thanks for today!")
                print("-"*150)
                exit()


            else:
                print("-"*150)
                print("Enter a valid choice!")
                print("-"*150)


    def display_action_menu(self) -> None:
        """
        Method with all methods implemented for signed in users
        """
        print("-"*150)
        print(f"Welcome to ReviewIT {self.logged_in_user}!")
        print("-"*150)

        while True:
            
            self.display_menu()
            menu_choice = input("Enter choice: ")


            if menu_choice == "1":
                self.display_reviews()


            elif menu_choice == "2":
                self.display_search_reviews()


            elif menu_choice == "3":
                self.display_add_review()


            elif menu_choice == "4":
                self.display_remove_review()


            elif menu_choice == "5":
                self.display_exit_menu()
                break
                

            else:
                self.display_error_menu()


Reviewitapp = ReviewITApp()