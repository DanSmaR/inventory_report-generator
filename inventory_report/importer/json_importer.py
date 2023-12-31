import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(json_file_path):
        file_extension = str(json_file_path).split(".")[-1]
        if file_extension != 'json':
            raise ValueError("Arquivo inválido")
        try:
            with open(json_file_path) as json_file:
                inventory = json.load(json_file)
                return inventory
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None
