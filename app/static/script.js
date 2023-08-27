console.log("file connected");

document.addEventListener('DOMContentLoaded', function () {
    const pdfInput = document.querySelector('.converter__input');
    const progressSpinner = document.getElementById('progressSpinner');
    const pdfPreview = document.getElementById('pdfPreview');
    const downloadBtn = document.querySelector('.converter__download-btn');
  
    pdfInput.addEventListener('change', function (event) {
      pdfPreview.innerHTML = ''; // Clear any previous content
      progressSpinner.style.display = 'block'; // Display spinner
      downloadBtn.style.display = 'none'; // Hide download button
      const file = event.target.files[0];
  
      // Simulate conversion delay
      setTimeout(() => {
        // After conversion (simulated delay)
        progressSpinner.style.display = 'none'; // Hide spinner
        downloadBtn.style.display = 'block'; // Show download button
        // Display PDF preview
        pdfPreview.innerHTML = `<embed src="${URL.createObjectURL(file)}" type="application/pdf" width="100%" height="600px">`;
      }, 2000); // Simulated delay in milliseconds
    });
  });
  