from review import Review


class Phone(Review):
    """
    Model for Phone
    """

    def __init__(self, review_username: str, product_id: int, product_name: str, product_supplier: str, product_price: int, product_review: str, product_grade: int, phone_screensize: int, phone_memory: int) -> None:
        """
        Constructor
        """
        super().__init__(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade)
        self.__phone_screensize = phone_screensize
        self.__phone_memory = phone_memory

    
    def get_phone_screensize(self) -> int:
        """
        Method for getting phone screensize
        """
        return self.__phone_screensize
    

    def get_phone_memory(self) -> int:
        """
        Method for getting phone memory
        """
        return self.__phone_memory
    

    def __str__(self) -> str:
        """
        Method for string formation
        """
        return (f"| Reviewer: {self.get_review_username()} | ID: {self.get_product_id()} | Supplier: {self.get_product_supplier()} | Name: {self.get_product_name()} | Price: {self.get_product_price()}$ | Screensize: {self.get_phone_screensize()}mm | Memory: {self.get_phone_memory()}GB | Review: '{self.get_product_review()}' | Grade: {self.get_product_grade()}/10 |")