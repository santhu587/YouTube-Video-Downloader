document.getElementById("downloadBtn").addEventListener("click", function() {
    const videoUrl = document.getElementById("url").value;

    if (!videoUrl) {
        document.getElementById("message").innerText = "Please enter a valid URL!";
        return;
    }

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: videoUrl }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("message").innerText = "Error: " + data.error;
        } else {
            document.getElementById("message").innerText = "Video Downloaded: " + data.title;
        }
    })
    .catch((error) => {
        document.getElementById("message").innerText = "An error occurred!";
    });
});
