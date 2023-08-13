const triggerUrl = "[API_GATEWAY_URL]/download";
const downloadButton = document.getElementById("download-button");
let tabUrl = "";

const setUrlAndUpdate = (tabs) => {
    tabUrl = tabs[0].url;
    const isYouTube = tabUrl.match("www\.youtube\.");
    const isVideo = tabUrl.match("v=[A-Za-z\d]+")
    if (isYouTube && isVideo) {
        downloadButton.removeAttribute("disabled");
    }
}

browser.tabs.query({ currentWindow: true, active: true }).then(setUrlAndUpdate);
downloadButton.addEventListener("click", () => {
    downloadButton.setAttribute("disabled", "disabled");
    downloadButton.innerText = "Download Pending";
    fetch(triggerUrl, {
        method: "POST",
        mode: "cors",
        headers: {
            Authorization: "[AUTH_KEY]",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ program_url: tabUrl })
    }).then((response) => {
        if (response.ok) {
            downloadButton.innerText = "Download Triggered";
        } else {
            downloadButton.innerText = `Error triggering download [${response.status}]`;
        }
    }).catch(() => {
        downloadButton.innerText = "Error triggering download";
    })
});
