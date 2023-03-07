from abc import ABC, abstractmethod


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(file_path):
        raise NotImplementedError
