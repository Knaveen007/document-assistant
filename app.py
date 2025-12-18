import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def extract_text_from_pdf(uploaded_file):
    """Extract text from uploaded PDF file"""
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def get_available_models():
    """Get list of available models"""
    try:
        models = genai.list_models()
        return [model.name for model in models if 'generateContent' in model.supported_generation_methods]
    except Exception as e:
        return []

def ask_question(context, question):
    """Use Google Gemini to answer questions based on document context"""
    try:
        # Get available models
        available_models = get_available_models()

        if not available_models:
            return "Error: No Gemini models available. Please check your API key and permissions."

        # Try available models
        for model_name in available_models[:3]:  # Try first 3 available models
            try:
                model = genai.GenerativeModel(model_name.replace('models/', ''))
                prompt = f"""You are a helpful assistant that answers questions based on the provided document content.

Document Content: {context}

Question: {question}

Answer based only on the document content:"""

                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                continue

        # If all models fail
        return f"Error: Could not use any available models. Available models: {available_models[:5]}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.set_page_config(page_title="AI Document Intelligence Assistant", page_icon="📄")

    # Initialize session state for question
    if "question" not in st.session_state:
        st.session_state.question = ""

    st.title("📄 AI Document Intelligence Assistant")
    st.markdown("Upload a document and ask questions about its content!")
    
    # File upload
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Extract text
        with st.spinner("Reading document..."):
            document_text = extract_text_from_pdf(uploaded_file)
        
        st.success(f"✅ Document loaded! ({len(document_text)} characters)")
        
        # Show document preview (first 500 chars)
        with st.expander("📋 Document Preview"):
            st.text(document_text[:500] + "..." if len(document_text) > 500 else document_text)
        
        # Question input
        question = st.text_input("💬 Ask a question about the document:", value=st.session_state.question, key="question_input")
        
        if question:
            with st.spinner("Analyzing document..."):
                answer = ask_question(document_text, question)
            
            st.markdown("### 🤖 Answer:")
            st.write(answer)
            
            # Additional suggestions
            st.markdown("---")
            st.markdown("**💡 Try asking:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Summarize key points"):
                    st.session_state.question = "Summarize the key points of this document."
                    st.rerun()
            with col2:
                if st.button("Main topics covered"):
                    st.session_state.question = "What are the main topics covered in this document?"
                    st.rerun()
            with col3:
                if st.button("Important findings"):
                    st.session_state.question = "What are the important findings in this document?"
                    st.rerun()

if __name__ == "__main__":
    main()
