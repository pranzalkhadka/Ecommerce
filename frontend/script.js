function searchProducts() {
    let searchTerm = document.getElementById('search-bar').value;
    console.log('Search Term:', searchTerm);

    fetch(`/api/search?query=${searchTerm}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => console.error('Error:', error));
}