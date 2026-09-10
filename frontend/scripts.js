async function uploadLog() {

    const fileInput = document.getElementById("logFile");
    const summary = document.getElementById("summary");

    if (fileInput.files.length === 0) {

        alert("Please select a log file.");
        return;

    }


    const file = fileInput.files[0];


    summary.textContent =
        "Analyzing logs with AI...\nPlease wait...";


    const formData = new FormData();

    formData.append("file", file);


    try {

        const response = await fetch(
            "http://13.60.10.175:8000/upload",
            {
                method: "POST",
                body: formData
            }
        );


        const result = await response.json();


        if (response.ok) {


            summary.textContent =
`✅ Upload Successful

Filename:
${result.filename}

--------------------------------

AI Summary

${result.summary}`;


            // Refresh log history after upload
            loadLogs();


        } 
        
        else {


            summary.textContent =
`❌ Error

${result.message}`;

        }


    } 
    
    catch(error) {


        summary.textContent =
`❌ Connection Failed

${error}`;

    }

}





async function loadLogs() {


    const table = document.getElementById("logTable");


    if (!table) {

        return;

    }


    try {


        const response = await fetch(
            "http://13.60.10.175:8000/logs"
        );


        const logs = await response.json();


        table.innerHTML = "";


        logs.forEach(log => {


            const row = document.createElement("tr");


            row.innerHTML = `

                <td>${log.timestamp || "-"}</td>

                <td>${log.server || "-"}</td>

                <td>${log.error_type || "-"}</td>

                <td>${log.message || "-"}</td>

                <td>${log.severity || "-"}</td>

                <td>${log.ai_summary || "-"}</td>

            `;


            table.appendChild(row);


        });


    } 
    
    catch(error) {


        console.log(
            "Failed to load logs:",
            error
        );

    }

}




// Load previous logs automatically when dashboard opens

window.onload = function() {

    loadLogs();

};
