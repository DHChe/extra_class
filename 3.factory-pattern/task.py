from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def export(self, data):
        pass

class PDFDocument(Document):
    def export(self, data):
        return f"PDFDocument: {data}"

class ExcelDocument(Document):
    def export(self, data):
        return f"ExcelDocument: {data}"

class Export(ABC):
    @abstractmethod
    def create_document(self):
        pass

    def save_document(self, data):
        doc = self.create_document()