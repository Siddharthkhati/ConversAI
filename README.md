# ConversAI: Chat with Multiple PDFs 📚🤖

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#TechStack)
- [Installation](#Installation)
- [Usage](#usage)


## Introduction 🎢
ConversAI is an intelligent chatbot application that allows users to upload and interact with multiple PDF documents. By leveraging advanced NLP and AI models, ConversAI enables seamless, meaningful, and accurate conversations based on the context of the uploaded PDFs.

Whether you’re analyzing research papers, reviewing lengthy contracts, or studying multiple documents, ConversAI provides a fast and intuitive way to extract information interactively.

## Features ⭐
- **PDF Upload:** Effortlessly upload one or multiple PDF files.
- **Contextual Understanding:** The chatbot answers queries using the content of uploaded PDFs as context.
- **Multi-document Support:** Handle queries across multiple documents simultaneously.
- **Secure & Scalable:** Quick and accurate responses to user questions.
- **Secure & Scalable:** Built on a robust backend, ensuring secure processing of your files.

## Tech Stack 🛠️
- **Frontend:** Streamlit for an intuitive and interactive user interface.
- **Backend:** Python for application logic, PyPDF2 for PDF processing.
- **AI/ML Models:** Google Generative AI, LangChain, FAISS for embeddings and conversational AI.
- **Storage:** FAISS for vector-based document storage and retrieval.

## Installation 🔧 
Follow the steps below to set up the project on your local system.

- **Prerequisites**
      -  Python 3.7 or later installed on your system.
      -  A valid Google API Key for Generative AI integration.
      -  Dependencies listed in requirements.txt.

## Usage 🚀
To start using the Multiple PDF Chatbot:

1. Run the application:
   ```
   streamlit run app.py 
   ```
2. Upload PDFs:
   ```
   Open a web browser and navigate to http://localhost:8501.
   ```

3. Ask Questions:
   ```
   Use the sidebar to upload one or more PDF documents.
   ```

4. Interactive Chat::
   ```
   View responses and ask follow-up questions to refine your understanding.
   ```
