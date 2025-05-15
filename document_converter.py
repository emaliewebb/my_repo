from abc import ABC, abstractmethod
from typing import Dict, Type


class DocumentConverter(ABC):
    """Abstract base class for document converters (Strategy Pattern)"""
    
    @abstractmethod
    def convert(self, content: str) -> str:
        """Convert document content from source format to target format"""
        pass


class PDFToTextConverter(DocumentConverter):
    """Converts PDF documents to plain text"""
    
    def convert(self, content: str) -> str:
        # In a real implementation, this would use a PDF parsing library
        print("Converting PDF to Text")
        return f"Text content extracted from PDF: {content[:50]}..."


class TextToHTMLConverter(DocumentConverter):
    """Converts plain text to HTML format"""
    
    def convert(self, content: str) -> str:
        print("Converting Text to HTML")
        # Simple conversion for demonstration
        html_content = f"<!DOCTYPE html>\n<html>\n<body>\n<p>{content}</p>\n</body>\n</html>"
        return html_content


class MarkdownToHTMLConverter(DocumentConverter):
    """Converts Markdown to HTML format"""
    
    def convert(self, content: str) -> str:
        print("Converting Markdown to HTML")
        # Simple conversion for demonstration (would use a markdown library in production)
        # Just handling basic markdown features for demonstration
        html_content = content.replace("# ", "<h1>") + "</h1>"
        return html_content


class ConverterFactory:
    """Factory for creating document converters (Factory Pattern)"""
    
    _converters: Dict[str, Type[DocumentConverter]] = {}
    
    @classmethod
    def register_converter(cls, source_format: str, target_format: str, converter: Type[DocumentConverter]):
        """Register a converter for a specific source-to-target format conversion"""
        key = f"{source_format.lower()}_to_{target_format.lower()}"
        cls._converters[key] = converter
    
    @classmethod
    def get_converter(cls, source_format: str, target_format: str) -> DocumentConverter:
        """Get the appropriate converter for the requested formats"""
        key = f"{source_format.lower()}_to_{target_format.lower()}"
        converter_class = cls._converters.get(key)
        
        if not converter_class:
            raise ValueError(f"No converter available for {source_format} to {target_format} conversion")
        
        return converter_class()


class DocumentConversionSystem:
    """Main class for the document conversion system"""
    
    def __init__(self):
        # Register available converters
        ConverterFactory.register_converter("pdf", "text", PDFToTextConverter)
        ConverterFactory.register_converter("text", "html", TextToHTMLConverter)
        ConverterFactory.register_converter("markdown", "html", MarkdownToHTMLConverter)
    
    def convert_document(self, content: str, source_format: str, target_format: str) -> str:
        """Convert a document from source format to target format"""
        converter = ConverterFactory.get_converter(source_format, target_format)
        return converter.convert(content)


# Example usage
if __name__ == "__main__":
    conversion_system = DocumentConversionSystem()
    
    # Example 1: Convert PDF to Text
    pdf_content = "This is a sample PDF document with some content."
    text_content = conversion_system.convert_document(pdf_content, "pdf", "text")
    print(f"Result: {text_content}\n")
    
    # Example 2: Convert Text to HTML
    text = "This is plain text that will be converted to HTML."
    html = conversion_system.convert_document(text, "text", "html")
    print(f"Result: {html}\n")
    
    # Example 3: Convert Markdown to HTML
    markdown = "# This is a Markdown Heading"
    html = conversion_system.convert_document(markdown, "markdown", "html")
    print(f"Result: {html}\n")