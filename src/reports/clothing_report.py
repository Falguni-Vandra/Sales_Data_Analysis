from .product_report import ProductReport


class ClothingReport(ProductReport):
    def generate_report(self):
        print("Generating Clothing Report...")
        return self.get_summary_statistics()
