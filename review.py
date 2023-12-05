from abc import abstractmethod


class Review:
    """
    Model for Review
    """

    def __init__(self, review_username: str, product_id: int, product_name: str, product_supplier: str, product_price: int, product_review: str, product_grade: int) -> None:
        """
        Constructor
        """
        self.__review_username = review_username
        # ID and timestamp should automatically be assigned to each review if the application would use a SQL or NoSQL database
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_supplier = product_supplier
        self.__product_price = product_price
        self.__product_review = product_review
        self.__product_grade = product_grade

    
    def get_review_username(self) -> str:
        """
        Method for getting the user of the review
        """
        return self.__review_username
    

    def get_product_id(self) -> int:
        """
        Method for getting product id
        """
        return self.__product_id
    

    def get_product_name(self) -> str:
        """
        Method for getting product name
        """
        return self.__product_name

    
    def get_product_supplier(self) -> str:
        """
        Method for getting product supplier
        """
        return self.__product_supplier


    def get_product_price(self) -> int:
        """
        Method for getting product price
        """
        return self.__product_price


    def get_product_review(self) -> str:
        """
        Method for getting product review
        """
        return self.__product_review


    def get_product_grade(self) -> int:
        """
        Method for getting product grade
        """
        return self.__product_grade


    @abstractmethod
    def __str__(self) -> None:
        """
        Method for string formation, will be implemented in subclasses 
        """
        pass