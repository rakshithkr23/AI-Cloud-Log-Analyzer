from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="AI Cloud Log Analyzer",
    description="A cloud-native application to collect, analyze, and summarize Linux logs using AWS and AI.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Cloud Log Analyzer",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.get("/project")
def project():
    return {
        "project": "AI Cloud Log Analyzer",
        "developer": "Rakshith Kumar",
        "features": [
            "Linux Log Collection",
            "Amazon S3 Upload",
            "AWS Lambda",
            "CloudWatch Integration",
            "Amazon Bedrock AI Analysis",
            "FastAPI REST API",
            "Dashboard"
        ]
    }
