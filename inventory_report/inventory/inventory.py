import csv
import json
from inventory_report.reports.complete_report import (
    CompleteReport,
    SimpleReport,
)


class Inventory:
    report_methods_lookup = {
        "simples": SimpleReport.generate,
        "completo": CompleteReport.generate,
    }

    @classmethod
    def import_data(cls, file_path, report_type):
        report_by_file_type_lookup = {
            'csv': cls.get_report_from_csv_file,
            'json': cls.get_report_from_json_file
        }
        file_type = str(file_path).split('.')[-1]
        return report_by_file_type_lookup[file_type](file_path, report_type)

    @classmethod
    def execute_report_method(cls, report_type, inventory):
        if report_type not in cls.report_methods_lookup:
            raise ValueError(
                "Incorret report type. Must be 'complete' or 'simple"
            )
        return cls.report_methods_lookup[report_type](inventory)

    @classmethod
    def get_report_from_csv_file(cls, csv_file_path, report_type):
        try:
            with open(csv_file_path, encoding="utf-8") as csv_file:
                inventory = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"'
                )
                return cls.execute_report_method(
                    report_type, list(inventory)
                )
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None

    @classmethod
    def get_report_from_json_file(cls, json_file_path, report_type):
        try:
            with open(json_file_path) as json_file:
                inventory = json.load(json_file)
                return cls.execute_report_method(
                    report_type, inventory
                )
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None
