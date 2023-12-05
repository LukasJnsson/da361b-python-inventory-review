

class Database:
    """
    Model for Database
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.__review_database = []


    def get_review_database(self) -> list:
        """
        Method for getting reviews from database
        """
        return self.__review_database