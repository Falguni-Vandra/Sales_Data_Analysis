import pandas as pd


class SalesData:
    """
    A class to handle sales data operations.
    """

    def __init__(self, file_path=None):
        """
        Initialize SalesData with optional file path.
        """
        self.__file_path = file_path
        self.__data = None

    def load_data(self):
        """
        Load data from a CSV file.
        """
        if self.__file_path:
            self.__data = pd.read_csv(self.__file_path)

    def set_data(self, data):
        """
        Directly set data, useful for testing.
        """
        self.__data = data

    def get_data(self):
        """
        Return the current data.
        """
        return self.__data

    def clean_data(self):
        """
        Clean the data by dropping NA values and converting types.
        """
        if self.__data is not None:
            self.__data.dropna(inplace=True)
            self.__data['Date'] = pd.to_datetime(self.__data['Date'])
            self.__data['Quantity'] = self.__data['Quantity'].astype(int)
            self.__data['Price'] = self.__data['Price'].astype(float)

    def get_sales_by_category(self, category):
        """
        Get sales data filtered by category.
        """
        if self.__data is not None:
            return self.__data[self.__data['Category'] == category]
        return None
