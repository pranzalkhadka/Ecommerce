function searchProducts() {
    let searchTerm = document.getElementById('search-bar').value;
    console.log('Search Term:', searchTerm);

    // Example AJAX request using fetch
    fetch(`/api/search?query=${searchTerm}`)
        .then(response => response.json())
        .then(data => {
            // Handle the response data (e.g., update UI with search results)
            console.log(data); // Example: Log the data to console
        })
        .catch(error => console.error('Error:', error));
}