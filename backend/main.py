from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import shutil

from backend.s3_upload import upload_log
from ai.bedrock_summary import summarize_logs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message":
        "AI Cloud Log Analyzer Running"
    }



@app.post("/upload")
async def upload_log(
    file: UploadFile = File(...)
):

    try:
        contents = await file.read()
        upload_to_s3(contents, file.filename)
        log_text = contents.decode("utf-8")
        summary = summarize_logs(log_text)

        return {
            "message": "Upload Successful",
            "filename": file.filename,
            "summary": summary
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


