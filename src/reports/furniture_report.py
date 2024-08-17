from .product_report import ProductReport


class FurnitureReport(ProductReport):
    def generate_report(self):
        print("Generating Furniture Report...")
        return self.get_summary_statistics()
