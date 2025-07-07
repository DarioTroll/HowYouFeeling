function setDefaultSonnoDates() {
    const today = new Date();
    const yesterday = new Date();
    yesterday.setDate(today.getDate() - 1);

    const toDateString = (date) => {
        return date.toISOString().split('T')[0]; // YYYY-MM-DD
    };

    const dataInizio = document.getElementById('data_inizio_sonno');
    const dataFine = document.getElementById('data_fine_sonno');

    if (dataInizio) dataInizio.value = toDateString(yesterday);
    if (dataFine) dataFine.value = toDateString(today);
}

window.addEventListener('DOMContentLoaded', setDefaultSonnoDates);
