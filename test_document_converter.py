import unittest
from my_repo.document_converter import DocumentConversionSystem, ConverterFactory, DocumentConverter


class MockConverter(DocumentConverter):
    """Mock converter for testing"""
    def convert(self, content: str) -> str:
        return f"MOCK_CONVERTED_{content}"


class DocumentConverterTests(unittest.TestCase):
    
    def setUp(self):
        self.conversion_system = DocumentConversionSystem()
    
    def test_pdf_to_text_conversion(self):
        pdf_content = "Sample PDF content"
        result = self.conversion_system.convert_document(pdf_content, "pdf", "text")
        self.assertIn("Text content extracted from PDF", result)
        self.assertIn(pdf_content[:10], result)
    
    def test_text_to_html_conversion(self):
        text_content = "Sample text content"
        result = self.conversion_system.convert_document(text_content, "text", "html")
        self.assertIn("<html>", result)
        self.assertIn("<body>", result)
        self.assertIn(text_content, result)
    
    def test_markdown_to_html_conversion(self):
        md_content = "# Heading"
        result = self.conversion_system.convert_document(md_content, "markdown", "html")
        self.assertIn("<h1>Heading</h1>", result)
    
    def test_unsupported_conversion(self):
        with self.assertRaises(ValueError):
            self.conversion_system.convert_document("content", "unsupported", "format")
    
    def test_factory_registration(self):
        # Register a new mock converter
        ConverterFactory.register_converter("test", "mock", MockConverter)
        
        # Get the converter and test it
        converter = ConverterFactory.get_converter("test", "mock")
        self.assertIsInstance(converter, MockConverter)
        
        # Test the conversion
        result = converter.convert("test_content")
        self.assertEqual(result, "MOCK_CONVERTED_test_content")


if __name__ == "__main__":
    unittest.main()