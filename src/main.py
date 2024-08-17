def main():
    from src.sales_data import SalesData
    from src.reports.electronics_report import ElectronicsReport
    from src.reports.furniture_report import FurnitureReport
    from src.reports.clothing_report import ClothingReport

    # Load and process data
    sales_data = SalesData(file_path="data/sales_data.csv")
    sales_data.load_data()
    sales_data.clean_data()

    # Generate reports
    electronics_report = ElectronicsReport(
        sales_data.get_sales_by_category("Electronics"))
    print(electronics_report.generate_report())

    furniture_report = FurnitureReport(
        sales_data.get_sales_by_category("Furniture"))
    print(furniture_report.generate_report())

    clothing_report = ClothingReport(
        sales_data.get_sales_by_category("Clothing"))
    print(clothing_report.generate_report())


if __name__ == "__main__":
    main()
