# Backend Application Setup

This project is a basic web application where users can upload a CV and a job description to receive a score for the CV and an explanation of the score.

## Setup Instructions

1. Clone this repository.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the root directory with the following content:
   ```
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   ```
   Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.
6. Run the FastAPI server:
   ```
   uvicorn main:app --reload
   ```
7. Access the API endpoints:
   - To upload a CV: `http://localhost:8000/upload/`
   - To get the CV score: `http://localhost:8000/cv_score/`

## Usage

- Upload a CV by sending a POST request to `/upload/` endpoint with the CV file.
- Use the received filename to get the CV score by sending a POST request to `/cv_score/` endpoint with the CV text.