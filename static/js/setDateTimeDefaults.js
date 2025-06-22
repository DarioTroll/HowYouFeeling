// static/js/setDateTimeDefaults.js

window.addEventListener('DOMContentLoaded', () => {
    const dataInput = document.getElementById('data');
    const oraInput = document.getElementById('ora');

    if (dataInput && oraInput) {
        const now = new Date();

        const yyyy = now.getFullYear();
        const mm = String(now.getMonth() + 1).padStart(2, '0');
        const dd = String(now.getDate()).padStart(2, '0');
        dataInput.value = `${yyyy}-${mm}-${dd}`;

        const hh = String(now.getHours()).padStart(2, '0');
        const min = String(now.getMinutes()).padStart(2, '0');
        oraInput.value = `${hh}:${min}`;
    }
});
