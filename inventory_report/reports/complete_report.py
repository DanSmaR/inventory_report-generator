from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        (
            oldest_manufacturing_date,
            nearest_expiration_date,
            company,
            product_qty_by_company
        ) = CompleteReport.get_simple_data(data)
        return f"""Data de fabricação mais antiga: {oldest_manufacturing_date}
Data de validade mais próxima: {nearest_expiration_date}
Empresa com mais produtos: {company}
{CompleteReport.get_companies_list_str(product_qty_by_company)}"""

    @staticmethod
    def get_companies_list_str(data: dict):
        list_companies_str = "Produtos estocados por empresa:\n"
        for company, qty in data.items():
            list_companies_str += f"- {company}: {qty}\n"
        return list_companies_str
