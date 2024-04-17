
document.getElementById('predictButton').onclick = function() {
    var formData = new FormData();
    var imageFile = document.getElementById('imageUpload').files[0];
    formData.append("image", imageFile);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText =
            'Predicted Class: ' + data.class + ', Confidence: ' + data.confidence.toFixed(4);
    })
    .catch(error => console.error('Error:', error));
};
