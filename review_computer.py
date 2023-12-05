from review import Review


class Computer(Review):
    """
    Model for Computer
    """

    def __init__(self, review_username: str, product_id: int, product_name: str, product_supplier: str, product_price: int, product_review: str, product_grade: int, computer_memory: int, computer_ram: int) -> None:
        """
        Constructor
        """
        super().__init__(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade)
        self.__computer_memory = computer_memory
        self.__computer_ram = computer_ram


    def get_computer_memory(self) -> int:
        """
        Method for getting memory of computer
        """
        return self.__computer_memory
    

    def get_computer_ram(self) -> int:
        """
        Method for getting ram of computer
        """
        return self.__computer_ram


    def __str__(self) -> str:
        """
        Method for string formation
        """
        return (f"| Reviewer: {self.get_review_username()} | ID: {self.get_product_id()} | Supplier: {self.get_product_supplier()} | Name: {self.get_product_name()} | Price: {self.get_product_price()}$ | Memory: {self.get_computer_memory()}GB | RAM: {self.get_computer_ram()}GB | Review: '{self.get_product_review()}' | Grade: {self.get_product_grade()}/10 |")