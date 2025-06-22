document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('darkModeToggle');
    const body = document.body;

    function applyDarkModePreference() {
        const darkMode = localStorage.getItem('darkMode');
        if (darkMode === 'enabled') {
            body.classList.add('dark-mode');
            if (toggleButton) toggleButton.textContent = 'Disattiva Dark Mode';
        } else {
            body.classList.remove('dark-mode');
            if (toggleButton) toggleButton.textContent = 'Attiva Dark Mode';
        }
    }

    function toggleDarkMode() {
        const darkMode = localStorage.getItem('darkMode');
        if (darkMode !== 'enabled') {
            localStorage.setItem('darkMode', 'enabled');
        } else {
            localStorage.setItem('darkMode', 'disabled');
        }
        applyDarkModePreference();
    }

    if (toggleButton) {
        toggleButton.addEventListener('click', toggleDarkMode);
    }

    applyDarkModePreference();
});
