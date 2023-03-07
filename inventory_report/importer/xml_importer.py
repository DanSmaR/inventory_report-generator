import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(xml_file_path):
        file_extension = str(xml_file_path).split(".")[-1]
        if file_extension != 'xml':
            raise ValueError("Arquivo inválido")
        try:
            with open(xml_file_path, "r") as xml_file:
                xml_string = xml_file.read()
                inventory = xmltodict.parse(xml_string)
                return inventory.get("dataset")["record"]
        except (IsADirectoryError, FileNotFoundError) as err:
            print(err)
            print("Wrong path name")
            return None
