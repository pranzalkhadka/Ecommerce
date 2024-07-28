document.getElementById('signin-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = 'logged_page.html'; // Redirect to asd.html on successful login
        } else {
            alert(data.message); // Display the error message from the server
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});