# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-10

### Added
- Initial release of AI Document Intelligence Assistant
- PDF document upload and text extraction functionality
- Question-answering capability using Google Gemini AI
- Streamlit web interface with file uploader
- Document preview feature (first 500 characters)
- Interactive question input with real-time answers
- Suggested question buttons for common queries (summarize, main topics, important findings)
- Environment variable configuration for API keys
- Error handling for Google Gemini API calls

### Dependencies
- streamlit
- google-generativeai
- PyPDF2
- python-dotenv

### Features
- Upload PDF documents
- Extract text content from PDFs
- Ask questions about document content
- Get AI-powered answers based on document context
- Preview document content
- Responsive web interface
