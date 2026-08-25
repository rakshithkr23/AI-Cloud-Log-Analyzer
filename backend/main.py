from fastapi import FastAPI, UploadFile, File
import shutil

from backend.s3_upload import upload_log
from ai.bedrock_summary import summarize_logs


app = FastAPI()


@app.get("/")
def home():

    return {
        "message":
        "AI Cloud Log Analyzer Running"
    }



@app.post("/analyze")
async def analyze_log(
    file: UploadFile = File(...)
):

    file_location = (
        f"logs/{file.filename}"
    )


    with open(
        file_location,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    upload_result = upload_to_s3(
        file_location
    )


    with open(
        file_location,
        "r"
    ) as log_file:

        logs = log_file.read()



    ai_result = summarize_logs(
        logs
    )


    return {

        "s3_status":
        upload_result,

        "ai_summary":
        ai_result
    }
