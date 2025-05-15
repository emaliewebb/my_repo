# Document Conversion System

A flexible system for converting documents between different formats using design patterns.

## Overview

This project implements a document conversion system that can transform documents between various formats. The implementation uses the Strategy and Factory design patterns to create a flexible, extensible architecture that follows SOLID principles.

## Features

- Convert documents between different formats
- Easily add new conversion formats
- Clean separation of concerns
- Extensible architecture

## Project Structure

- `document_converter.py` - Main implementation with Strategy and Factory patterns
- `test_document_converter.py` - Unit tests for the conversion system
- `technical_document.md` - Technical documentation explaining design choices

## Design Patterns Used

1. **Strategy Pattern** - Encapsulates different conversion algorithms
2. **Factory Pattern** - Creates appropriate converters based on input/output formats

## Running the Code

To run the example:

```bash
python document_converter.py
```

To run the tests:

```bash
python test_document_converter.py
```

## Adding New Converters

To add a new converter:

1. Create a new class that inherits from `DocumentConverter`
2. Implement the `convert` method
3. Register the converter with the `ConverterFactory`

Example:

```python
class JSONToXMLConverter(DocumentConverter):
    def convert(self, content: str) -> str:
        # Implementation here
        return xml_content

# Register the new converter
ConverterFactory.register_converter("json", "xml", JSONToXMLConverter)
```