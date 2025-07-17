# MindScope_AI_Chatbot
MindScope AI is an intelligent mental health companion built using Streamlit, Langchain, and Google Gemini APIs. It enables anonymous conversations, detects mental well-being patterns, and offers personalized self-care guidance — all in a beautiful and secure interface.

## 📁 Project Structure

MindScope-AI/
│
├── app.py               # Main Streamlit app file
├── htmlTemplate.py      # Custom HTML templates for chatbot UI
├── requirements.txt     # Python dependencies
├── .env                 # Your Google Gemini API key (not committed)
├── README.md            # Project documentation
└── assets/              # (Optional) Avatar images or screenshots


## Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Set up API Key
Create .env file own.
format like below: 
GOOGLE_API_KEY=your_api_key_here

## Run the App
streamlit run app.py

## 💡 Use Cases
Mental health journaling

Self-reflection assistant

Well-being chat support (non-diagnostic)

Anonymous safe space for thoughts
