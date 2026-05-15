const chatHistory = [];

async function sendPrompt() {
    const prompt = document.getElementById("prompt").value;

    const token = localStorage.getItem("access");

    chatHistory.push({
        role: "user",
        content: prompt
    });

    const res = await fetch("/chat/prompt/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            messages: chatHistory
        })
    });

    const data = await res.json();

    const jobId = data.job_id;

    addMessage("You", prompt);
    addMessage("AI", "...");

    pollJob(jobId);
}

async function pollJob(jobId) {
    const token = localStorage.getItem("access");

    const interval = setInterval(async () => {
        try {
            const res = await fetch(`/chat/prompt/${jobId}/`, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });

            const data = await res.json();

            console.log("JOB STATUS RESPONSE:", data);
            console.log("STATUS:", data.status);

            if (data.status.toLowerCase() === "done") {
                clearInterval(interval);

                replaceLastMessage(data.response);

                chatHistory.push({
                    role: "assistant",
                    content: data.response
                });
            }

            if (data.status === "failed") {
                clearInterval(interval);
                replaceLastMessage("Error: " + data.error);
            }

        } catch (err) {
            console.error("Polling error:", err);
        }

    }, 1000);
}

function addMessage(role, text) {
    const div = document.getElementById("chat");
    div.innerHTML += `<p><b>${role}:</b> ${text}</p>`;
}

function replaceLastMessage(text) {
    const div = document.getElementById("chat");
    const messages = div.getElementsByTagName("p");
    messages[messages.length - 1].innerHTML = `<b>AI:</b> ${text}`;
}

async function logout() {
    const refresh = localStorage.getItem("refresh");

    const access = localStorage.getItem("access");

    try {
        await fetch("/user/logout/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${access}`
            },
            body: JSON.stringify({
                refresh: refresh
            })
        });

    } catch (e) {
        console.error("Logout error:", e);
    }

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    window.location.href = "/chat/login";
}