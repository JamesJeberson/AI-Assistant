# AI Assistant with Dynamic Personalities

## Overview
This project implements an AI-powered chatbot application leveraging IBM WatsonxGPT models. The application supports different tones and models, offering dynamic AI responses. Users interact with the chatbot through a web interface built using HTML, CSS, and JavaScript. The backend processes requests with Python and Flask, integrating IBM Watsonx APIs to generate model-specific responses. 

The application allows users to:
- Select one of three AI models: **Llama3**, **Granite**, or **Mixtral**.
- Choose the tone of the AI responses: **Formal**, **Casual**, or **Cheerful**.
- Receive real-time AI-generated responses in a conversational format.

## Demo
![Demo GIF](static/demo.gif)

## Features
- **Multi-model Support**: Integrates three powerful AI models: Llama3, Granite, and Mixtral.
- **Tone Selection**: Provides personalized responses based on the selected tone.
- **User-friendly Interface**: A clean and responsive chat interface with message bubbles.
- **Error Handling**: Handles invalid inputs and errors gracefully.

## Technologies Used
### Backend
- **Python**
- **Flask**: Framework to handle API routes and serve the frontend.
- **IBM Watsonx**: APIs for leveraging powerful generative AI models.
- **LangChain**: Used for model initialization and prompt handling.
- **Pydantic**: Defines structured data models for AI response parsing.

### Frontend
- **HTML5, CSS3, and JavaScript**: For creating an intuitive and responsive user interface.
- **Fetch API**: Handles AJAX requests to the Flask backend.

### Miscellaneous
- **IBM Watsonx LLMs**: Implements Meta Llama, IBM Granite, and Mistral Mixtral models.
- **JSON**: For structured data exchange between frontend and backend.

## File Structure
```
.
├── app.py          # Flask application
├── model.py        # AI models, templates, and response generation logic
├── config.py       # Configuration file for model parameters and credentials
├── templates
│   └── index.html  # Frontend HTML file
├── static
│   └── demo.gif    # Demo GIF showcasing the application
└── README.md       # Documentation
```

## How to Run the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/ai-assistant-watsonx](https://github.com/JamesJeberson/AI-Assistant-with-Dynamic-Personalities
    cd AI-Assistant-with-Dynamic-Personalities
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up IBM Watsonx credentials:
   - Update the `CREDENTIALS` dictionary in `config.py` with your IBM Cloud API details.

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Open the browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

6. Start interacting with the AI assistant!

## Requirements
- Python 3.8+
- Flask
- IBM Watsonx API credentials
- LangChain
- Pydantic
