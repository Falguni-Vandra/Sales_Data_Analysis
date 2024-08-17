# Sales Data Analysis

## Overview

This project performs sales data analysis and generates reports based on sales categories using Python. It utilizes pandas for data manipulation and includes custom reports for different sales categories.

## Features

- **Data Cleaning:** Cleans the sales data by handling missing values and converting data types.
- **Sales Reporting:** Generates detailed reports for different sales categories including Electronics, Furniture, and Clothing.
- **Testing:** Includes unit tests to verify the correctness of data processing and reporting.

## Getting Started

### Prerequisites

- Python 3.x
- Pandas
- Pytest
- Pylint

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Falguni-Vandra/Sales_Data_Analysis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Sales_Data_Analysis
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required packages:

    ```bash
    pip install pandas pytest pylint
    ```

### Usage

1. **Load Data:**
   - Place your sales data CSV file in the `data/` directory (if applicable).

2. **Run the Analysis:**
   - You can run the main script to execute data analysis and generate reports. Ensure to replace `"data/sales_data.csv"` with your actual file path.

    ```python
    from src.sales_data import SalesData
    from src.reports.electronics_report import ElectronicsReport
    from src.reports.furniture_report import FurnitureReport
    from src.reports.clothing_report import ClothingReport

    # Initialize and load data
    sales_data = SalesData(file_path="data/sales_data.csv")
    sales_data.load_data()
    sales_data.clean_data()

    # Generate reports
    electronics_report = ElectronicsReport(sales_data.get_sales_by_category("Electronics"))
    print(electronics_report.generate_report())

    furniture_report = FurnitureReport(sales_data.get_sales_by_category("Furniture"))
    print(furniture_report.generate_report())

    clothing_report = ClothingReport(sales_data.get_sales_by_category("Clothing"))
    print(clothing_report.generate_report())
    ```

3. **Run Tests:**
   - To run the tests and verify functionality, use:

    ```bash
    pytest
    ```

4. **Lint Code:**
   - To check the code quality, use:

    ```bash
    pylint src tests
    ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## Acknowledgements

- Thanks to the open-source community for the tools and libraries used in this project.
