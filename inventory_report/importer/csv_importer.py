import csv
from importer import Importer


class CsvImporter(Importer):
    def import_data(csv_file_path):
        file_extension = str(csv_file_path).split(".")[-1]
        if file_extension != 'csv':
            raise ValueError("Arquivo inválido")
        try:
            with open(csv_file_path, encoding="utf-8") as csv_file:
                inventory = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"'
                )
                return list(inventory)
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None
