from database import Database
from review_watch import SmartWatch
from review_phone import Phone
from review_computer import Computer
from review import Review


class ReviewIT:
    """
    Model for ReviewIT
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.database = Database()


    def get_review_database(self) -> list:
        """
        Method for getting data from database
        """
        reviews = self.database.get_review_database()
        return reviews

    
    def add_review_smartwatch(self, review_username: str, product_id: int, product_name: str, product_supplier: str, product_price: int, product_review: str, product_grade: int, watch_diameter: int, watch_strap: str) -> None:
        """
        Method for adding new review of a smartwatch to the database
        """
        new_review_smartwatch = SmartWatch(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade, watch_diameter, watch_strap)
        self.database.get_review_database().append(new_review_smartwatch)


    def add_review_phone(self, review_username: str, product_id: int, product_name: str, product_supplier: str, product_price: int, product_review: str, product_grade: int, phone_screensize: int, phone_memory: int) -> None:
        """
        Method for adding new review of a phone to the database
        """
        new_review_phone = Phone(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade, phone_screensize, phone_memory)
        self.database.get_review_database().append(new_review_phone)
    

    def add_review_computer(self, review_username: str, product_id: int, product_name: str, product_supplier: str, product_price: int, product_review: str, product_grade: int, computer_memory: int, computer_ram: int) -> None:
        """
        Method for adding new review of a computer to the database
        """
        new_review_computer = Computer(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade, computer_memory, computer_ram)
        self.database.get_review_database().append(new_review_computer)


    def get_search_review(self, search_input) -> list:
        """
        Method to search for reviews in database
        """
        results = []
        for review in self.get_review_database():
            if search_input in review.get_product_name():
                results.append(review)
        return results


    def get_remove_review(self, remove_input) -> bool:
        """
        Method to remove review from database
        """
        for review in self.get_review_database():
            if remove_input in review.get_product_name():
                self.get_review_database().remove(review)
                return True
        return False