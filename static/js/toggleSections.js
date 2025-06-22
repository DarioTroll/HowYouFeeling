// static/js/toggleSections.js

function toggleSection(header) {
    const content = header.nextElementSibling;
    if(content.style.display === "block"){
        content.style.display = "none";
        header.textContent = header.textContent.replace("▲", "▼");
    } else {
        content.style.display = "block";
        header.textContent = header.textContent.replace("▼", "▲");
    }
}
