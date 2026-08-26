async function uploadLog() {

    const fileInput = document.getElementById("logFile");
    const summary = document.getElementById("summary");

    if (fileInput.files.length === 0) {
        alert("Please select a log file.");
        return;
    }

    const file = fileInput.files[0];

    // Show loading message
    summary.textContent = "Analyzing logs with AI...\nPlease wait...";

    // Create form data
    const formData = new FormData();
    formData.append("file", file);

    try {

        const response = await fetch("http://13.60.10.175:8000/upload", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (response.ok) {

            summary.textContent =
`✅ Upload Successful

Filename:
${result.filename}

----------------------------------------

AI Summary

${result.summary}`;

        } else {

            summary.textContent =
`❌ Error

${result.message}`;

        }

    } catch (error) {

        summary.textContent =
`❌ Connection Failed

${error}`;
    }
}
