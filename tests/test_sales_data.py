import pytest
import pandas as pd
from src.sales_data import SalesData
from src.reports.electronics_report import ElectronicsReport
from src.reports.furniture_report import FurnitureReport
from src.reports.clothing_report import ClothingReport


@pytest.fixture
def sales_data_fixture():
    """
    Fixture to provide a SalesData instance with test data.
    """
    data = {
        'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        'Product': ['Smartphone', 'Laptop', 'Sofa', 'T-shirt'],
        'Category': ['Electronics', 'Electronics', 'Furniture', 'Clothing'],
        'Quantity': [10, 5, 2, 50],
        'Price': [700, 1200, 1500, 25]
    }
    df = pd.DataFrame(data)

    sales_data_instance = SalesData()
    sales_data_instance.set_data(df)
    return sales_data_instance


def test_clean_data(sales_data_fixture):
    """
    Test data cleaning functionality.
    """
    sales_data_fixture.clean_data()
    assert sales_data_fixture.get_data().isnull().sum().sum() == 0


def test_electronics_report(sales_data_fixture):
    """
    Test the report generation for electronics sales.
    """
    electronics_data = sales_data_fixture.get_sales_by_category("Electronics")
    electronics_report = ElectronicsReport(electronics_data)
    report = electronics_report.generate_report()
    assert report['Total Sales'] == 13000


def test_furniture_report(sales_data_fixture):
    """
    Test the report generation for furniture sales.
    """
    furniture_data = sales_data_fixture.get_sales_by_category("Furniture")
    furniture_report = FurnitureReport(furniture_data)
    report = furniture_report.generate_report()
    assert report['Total Sales'] == 3000


def test_clothing_report(sales_data_fixture):
    """
    Test the report generation for clothing sales.
    """
    clothing_data = sales_data_fixture.get_sales_by_category("Clothing")
    clothing_report = ClothingReport(clothing_data)
    report = clothing_report.generate_report()
    assert report['Total Sales'] == 1250
