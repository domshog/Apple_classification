async function predict() {
    const fileInput = document.getElementById('fileInput');
    const result = document.getElementById('result');
    
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });
    
    const data = await response.json();
    result.textContent = `Prediction: ${data.prediction}`;
}
