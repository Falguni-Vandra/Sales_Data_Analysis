from .product_report import ProductReport


class ElectronicsReport(ProductReport):
    def generate_report(self):
        print("Generating Electronics Report...")
        return self.get_summary_statistics()
