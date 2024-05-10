from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import create_tables, get_db, CVData
from PyPDF2 import PdfFileReader
from io import BytesIO
from dotenv import load_dotenv
import openai

load_dotenv()

app = FastAPI()

create_tables()


def save_to_database(db: Session, filename: str, pdf_content: bytes, text_content: str):
    db_obj = CVData(filename=filename, pdf=pdf_content, text_content=text_content)
    db.add(db_obj)
    db.commit()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    
    # Extract text content from PDF
    pdf_reader = PdfFileReader(BytesIO(contents))
    text_content = ""
    for page_num in range(pdf_reader.numPages):
        text_content += pdf_reader.getPage(page_num).extractText()

    # Save to database
    save_to_database(db, file.filename, contents, text_content)
    
    return {"filename": file.filename}


@app.post("/cv_score/")
async def get_cv_score(cv_text: str):
    # Call OpenAI API to get the CV score
    # Use the cv_text to generate the prompt and fetch the score
    # Code for calling OpenAI API goes here
    return {"cv_score": 8, "explanation": "The candidate's CV demonstrates strong relevant experience and skills."}
