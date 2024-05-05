async function fetchMatchingClothes(hexCode) {
    const url = 'http://127.0.0.1:5000/match';  // Endpoint for the POST request
    const data = {
        Hex: hexCode  // Prepare the JSON payload with the hex code
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)  // Convert the JavaScript object to a JSON string
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const matches = await response.json();  // Parse the JSON response
        displayImages(matches);  // Call to display images
    } catch (error) {
        console.error('Error fetching matching clothes:', error);
        displayImages([]);  // Ensure clear display if error occurs
    }
}

function displayImages(imageData) {
    const container = document.getElementById('imagesContainer');
    container.innerHTML = '';  // Clear previous images

    imageData.forEach(image => {
        const img = document.createElement('img');
        img.src = image.filePath.replace(/\\/g, '/'); // Correct the file path
        img.alt = `Clothing item ${image.id}`;
        container.appendChild(img);
    });
}

function fetchAndDisplay(hexCode) {
    fetchMatchingClothes(hexCode).then(matches => {
        console.log('Matching clothes:', matches);
    }).catch(error => {
        console.error('Failed to fetch matches:', error);
    });
}