from scripts.dynamodb_store import store_log


log = {
    "level": "ERROR",
    "message": "Apache server failed"
}


store_log(
    log,
    "Web server is not responding"
)


print("Stored successfully")
