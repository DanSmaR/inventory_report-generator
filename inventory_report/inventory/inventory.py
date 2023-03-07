import csv
import json
import xmltodict
from inventory_report.reports.complete_report import (
    CompleteReport,
    SimpleReport,
)


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        report_by_file_type_lookup = {
            "csv": cls.get_report_from_csv_file,
            "json": cls.get_report_from_json_file,
            "xml": cls.get_report_from_xml_file,
        }
        try:
            file_type = str(file_path).split(".")[-1]
            return report_by_file_type_lookup[file_type](
                file_path, report_type
            )
        except KeyError as err:
            print(err)
            print('Incorrect file extension. Must be "csv", "json" or "xml".')
            return None

    @staticmethod
    def execute_report_method(report_type, inventory):
        report_methods_lookup = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }
        if report_type not in report_methods_lookup:
            raise ValueError(
                "Incorret report type. Must be 'complete' or 'simple"
            )
        return report_methods_lookup[report_type](inventory)

    @classmethod
    def get_report_from_csv_file(cls, csv_file_path, report_type):
        try:
            with open(csv_file_path, encoding="utf-8") as csv_file:
                inventory = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"'
                )
                return cls.execute_report_method(report_type, list(inventory))
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None

    @classmethod
    def get_report_from_json_file(cls, json_file_path, report_type):
        try:
            with open(json_file_path) as json_file:
                inventory = json.load(json_file)
                return cls.execute_report_method(report_type, inventory)
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None

    @classmethod
    def get_report_from_xml_file(cls, xml_file_path, report_type):
        try:
            with open(xml_file_path, "r") as xml_file:
                xml_string = xml_file.read()
                inventory = xmltodict.parse(xml_string)
                return cls.execute_report_method(
                    report_type, inventory.get("dataset")["record"]
                )
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None
