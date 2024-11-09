# Image Conversational Chatbot

Welcome to the Image Conversational Chatbot project, a visual question-answering system designed to interact with users through image-based queries, specifically focused on automotive topics. This chatbot leverages a combination of BLIP-2 and Cohere APIs for an enriched, conversational experience. The chatbot operates on a single page, allowing users to upload an image, ask questions, and receive relevant information about cars, including engine details, model specifications, and more.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Overview

The Image Conversational Chatbot is a visual question-answering system developed to interact with users using image inputs and text queries. The bot is capable of answering car-related questions by analyzing images of vehicles and using a fine-tuned BLIP-2 model combined with Cohere’s NLP capabilities to generate conversational responses.

---

## Features
- **Image Recognition and Text-Based Queries**: Upload car images and ask questions for instant responses.
- **Domain-Specific Knowledge**: Provides detailed information about images and additional details.
- **Cohere Integration**: Enhances response quality by making answers more conversational.
- **Single Page Interaction**: Streamlined user experience on a single chat page.

---

## Technologies Used
- **Python**: Main programming language.
- **Flask**: Backend framework for web server deployment.
- **BLIP-2**: Image processing model for understanding car images.
- **Cohere API**: For generating and refining conversational text.
- **HTML/CSS**: For front-end design.
- **JavaScript**: Enabling interactive elements on the result page.
- **CUDA-enabled GPU**: For efficient model inference (recommended).
- **PyTorch 2.5.1 and cuda 12.1**: Deep learning library with CUDA support.


---

## Installation

### Prerequisites
- Python 3.8+
- [Cohere API key](https://cohere.com/) (trial or paid)
- BLIP-2 model files
- CUDA-enabled GPU (optional for faster inference) 12.1
- PyTorch 2.5.1 (compatible with CUDA for GPU acceleration)

### Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/username/image-conversational-chatbot.git
    cd image-conversational-chatbot
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure API Keys**
   - Create a `.env` file in the project root:
     ```plaintext
     COHERE_API_KEY=your_cohere_api_key
     ```
   - Replace `your_cohere_api_key` with your Cohere API key.

5. **Run the Application**
    ```bash
    python app.py
    ```

6. **Access the Chatbot**
   Open a web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage

1. **Upload an Image**: Click on the "Upload Image" button and select a car image.
2. **Ask a Question**: Enter a car-related question (e.g., "What model is this?" or "What engine specifications does this car have?").
3. **Receive an Answer**: The chatbot will display an answer with information about the car in the uploaded image.
4. **Conversational Flow**: Continue asking follow-up questions for additional information.

---

## Project Structure

```plaintext
image-conversational-chatbot/
├── app.py                 # Flask app and server configurations
├── static/                # Contains CSS and images
│   ├── style.css/
│   └── uploads/            #uploads folder that contains all uploaded images
├── templates/             # HTML template for chat page
│   ├── chat.html
├── models/                # Model files for BLIP-2 and Cohere integration
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation
├──  save_model.ipynb       #script for saving model locally from huggingface
