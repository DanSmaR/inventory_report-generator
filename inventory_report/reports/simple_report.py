import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        (
            oldest_manufacturing_date,
            nearest_expiration_date,
            company,
        ) = SimpleReport.get_simple_data(data)
        return f"""Data de fabricação mais antiga: {oldest_manufacturing_date}
Data de validade mais próxima: {nearest_expiration_date}
Empresa com mais produtos: {company}"""

    @staticmethod
    def get_simple_data(data):
        min_exp_days = None
        max_manuf_days = None
        oldest_manufacturing_date = None
        nearest_expiration_date = None
        today_date = datetime.datetime.today().date()
        product_qty_by_company = dict()

        for item in data:
            item_exp_date = datetime.datetime.strptime(
                str(item.get("data_de_validade")), "%Y-%m-%d"
            ).date()
            item_manufac_date = datetime.datetime.strptime(
                str(item.get("data_de_fabricacao")), "%Y-%m-%d"
            ).date()
            (
                min_exp_days,
                nearest_expiration_date,
            ) = SimpleReport.get_min_expiration_date(
                min_exp_days,
                today_date,
                item_exp_date,
                nearest_expiration_date,
            )

            (
                max_manuf_days,
                oldest_manufacturing_date,
            ) = SimpleReport.get_max_manuf_date(
                max_manuf_days,
                today_date,
                item_manufac_date,
                oldest_manufacturing_date,
            )

            SimpleReport.update_products_qty_by_company(
                item, product_qty_by_company
            )
        most_freq_company = SimpleReport.get_most_freq_company(
            product_qty_by_company
        )

        return (
            oldest_manufacturing_date.strftime("%Y-%m-%d"),
            nearest_expiration_date.strftime("%Y-%m-%d"),
            most_freq_company,
        )

    @staticmethod
    def get_most_freq_company(product_qty_by_company):
        companies_list = [
            (qty, company) for company, qty in product_qty_by_company.items()
        ]
        return sorted(companies_list, reverse=True)[0][1]

    @staticmethod
    def update_products_qty_by_company(item, product_qty_by_company):
        if not product_qty_by_company.get(item["nome_da_empresa"]):
            product_qty_by_company[item["nome_da_empresa"]] = 1
        else:
            product_qty_by_company[item["nome_da_empresa"]] += 1

    @staticmethod
    def get_max_manuf_date(
        max_manuf_days,
        today_date,
        item_manufac_date,
        oldest_manufacturing_date,
    ):
        days_since_manuf = today_date - item_manufac_date
        if not max_manuf_days:
            return (days_since_manuf.days, item_manufac_date)
        if days_since_manuf.days > max_manuf_days:
            return (days_since_manuf.days, item_manufac_date)
        return (max_manuf_days, oldest_manufacturing_date)

    @staticmethod
    def get_min_expiration_date(
        min_exp_days, today_date, item_exp_date, nearest_expiration_date
    ):
        days_to_expire = item_exp_date - today_date
        if days_to_expire.days <= 0:
            return (min_exp_days, nearest_expiration_date)
        if not min_exp_days:
            return (days_to_expire.days, item_exp_date)
        if days_to_expire.days < min_exp_days:
            return (days_to_expire.days, item_exp_date)
        return (min_exp_days, nearest_expiration_date)
