from abc import ABC, abstractmethod


class ProductReport(ABC):
    def __init__(self, sales_data):
        self.sales_data = sales_data

    @abstractmethod
    def generate_report(self):
        pass

    def get_summary_statistics(self):
        total_sales = (self.sales_data['Quantity'] *
                       self.sales_data['Price']).sum()
        avg_sales = (self.sales_data['Quantity'] *
                     self.sales_data['Price']).mean()
        return {'Total Sales': total_sales, 'Average Sales': avg_sales}
