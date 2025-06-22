// static/js/formSubmitHandler.js

function handleFormSubmit(formId, endpoint, options = {}) {
    document.addEventListener('DOMContentLoaded', () => {
        const form = document.getElementById(formId);
        if (!form) return;

        form.addEventListener('submit', function (event) {
            event.preventDefault();

            const formData = new FormData(form);

            fetch(endpoint, {
                method: 'POST',
                body: formData
            })
            .then(resp => resp.json())
            .then(data => {
                if (data.success) {
                    alert("✅ " + data.message);
                    if (options.reset) form.reset();
                    if (options.reload) location.reload();
                } else {
                    alert("❌ " + data.message);
                }
            })
            .catch(() => {
                if (options.feedbackId) {
                    const feedback = document.getElementById(options.feedbackId);
                    if (feedback) {
                        feedback.style.color = 'red';
                        feedback.textContent = 'Errore di rete o server.';
                    }
                } else {
                    alert("❌ Errore di rete o server.");
                }
            });
        });
    });
}
