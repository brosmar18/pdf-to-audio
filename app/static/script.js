console.log("file connected");

document.addEventListener('DOMContentLoaded', function () {
    const pdfInput = document.querySelector('.converter__input');
    const progressSpinner = document.getElementById('progressSpinner');

    pdfInput.addEventListener('change', function (event) {
        progressSpinner.style.display = 'block';
        const file = event.target.files[0];
        if (file.type === 'application/pdf') {
            const pdfPreview = document.getElementById('pdfPreview');
            pdfPreview.innerHTML = `<embed src="${URL.createObjectURL(file)}" type="application/pdf" width="100%" height="600px">`;
        }

        // Simulate conversion delay 
        setTimeout(() => {
            progressSpinner.style.display = "none"; // Hide spinner
        }, 2000); // simulated delay in milliseconds
    });
});