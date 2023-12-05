from review import Review


class SmartWatch(Review):
    """
    Model for SmartWatch
    """

    def __init__(self, review_username: str, product_id: int, product_name: str, product_supplier: str, product_price: int, product_review: str, product_grade: int, watch_diameter: int, watch_strap: str) -> None:
        """
        Constructor
        """
        super().__init__(review_username, product_id, product_name, product_supplier, product_price, product_review, product_grade)
        self.__watch_diameter = watch_diameter
        self.__watch_strap = watch_strap


    def get_watch_diameter(self) -> int:
        """
        Metod for getting diameter of watch
        """
        return self.__watch_diameter

    
    def get_watch_strap(self) -> str:
        """
        Method for getting strap of watch
        """
        return self.__watch_strap


    def __str__(self) -> str:
        """
        Method for string formation
        """
        return (f"| Reviewer: {self.get_review_username()} | ID: {self.get_product_id()} | Supplier: {self.get_product_supplier()} | Name: {self.get_product_name()} | Price: {self.get_product_price()}$ | Diameter: {self.get_watch_diameter()}mm | Strap: {self.get_watch_strap()} | Review: '{self.get_product_review()}' | Grade: {self.get_product_grade()}/10 |")