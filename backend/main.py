import os
import uuid
from dotenv import load_dotenv
from backend.s3_upload import upload_to_s3
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from scripts.dynamodb_store import (
        store_log,
        get_all_logs,
        get_log_by_id,
        get_high_severity_logs
        )
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")

app = FastAPI(title="AI Cloud Log Analyzer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Cloud Log Analyzer API is running",
            "region" : AWS_REGION,
            "bucket": S3_BUCKET
            }

@app.post("/upload")
async def upload_log(file: UploadFile = File(...)):
    os.makedirs("logs", exist_ok = True)
    
    log_id = str(uuid.uuid4())
    file_location = f"logs/{file.filename}"
    file_content = await file.read()
    
    with open(file_location, "wb") as buffer:
        buffer.write(file_content)

        log_data = {
                "level" : "ERROR",
                "message" : "Log file uploaded"}
        ai_summary = "Waiting for AI analysis"
        
        store_log(
                log_id,
                log_data,
                ai_summary
                )
        s3_result = upload_to_s3(
                file_content,
                file.filename
                )

    return {
            "log_id": log_id,
        "filename": file.filename,
        "message": "File uploaded successfully",
        "summary": ai_summary,
        "s3_upload": s3_result
    }

@app.get("/health")
def health():
    return {"status" : "healthy"}

@app.get("/logs")
def fetch_logs():
    return get_all_logs()


@app.get("/logs/{log_id}")
def fetch_log(log_id: str):
    log = get_log_by_id(log_id)

    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    return log


@app.get("/logs/high")
def fetch_high_logs():
    return get_high_severity_logs()
