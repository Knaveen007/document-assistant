# AI Document Intelligence Assistant

A powerful Streamlit-based web application that allows users to upload PDF documents and ask intelligent questions about their content using Google's Gemini AI model.

## Features

- 📄 **PDF Upload & Processing**: Upload PDF documents and extract text content automatically
- 🤖 **AI-Powered Q&A**: Ask questions about your documents and get intelligent answers
- 👀 **Document Preview**: View a preview of the document content before asking questions
- 💡 **Smart Suggestions**: Pre-built question suggestions for common queries
- 🔒 **Secure API Handling**: Environment variable configuration for API keys
- 🎨 **Modern UI**: Clean, responsive Streamlit interface

## Prerequisites

- Python 3.7+
- Google API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd document-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided local URL (usually `http://localhost:8501`)

3. Upload a PDF document using the file uploader

4. Ask questions about the document content in the text input field

5. View the AI-generated answers based on the document context

## Requirements

- streamlit
- google-generativeai
- PyPDF2
- python-dotenv

## Project Structure

```
document-assistant/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this file)
├── README.md             # Project documentation
└── CHANGELOG.md          # Version history
```

## How It Works

1. **Document Upload**: Users upload PDF files through the Streamlit interface
2. **Text Extraction**: PyPDF2 library extracts text content from all pages of the PDF
3. **Question Processing**: User questions are sent to Google's Gemini AI model along with the document context
4. **AI Response**: The model generates answers based solely on the provided document content
5. **Display Results**: Answers are displayed in the web interface with additional suggestion buttons

## Configuration

The application uses environment variables for configuration:

- `GOOGLE_API_KEY`: Your Google API key (required)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.
