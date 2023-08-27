console.log("file connected");

document.addEventListener('DOMContentLoaded', function () {
    const pdfInput = document.querySelector('.converter__input');

    pdfInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file.type === 'application/pdf') {
            const pdfPreview = document.getElementById('pdfPreview');
            pdfPreview.innerHTML = `<embed src="${URL.createObjectURL(file)}" type="application/pdf" width="100%" height="600px">`;
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const pdfTextElement = document.getElementById('pdfText');
    pdfTextElement.innerText = "{{ extracted_text }}";
});