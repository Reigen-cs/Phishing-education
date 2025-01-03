// Add event listener to the form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Get form values
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    // Simple validation checks
    if (username === "" || password === "") {
        // Show error message if fields are empty
        const errorMessage = document.getElementById('errorMessage');
        errorMessage.textContent = "Both fields are required.";
        errorMessage.style.display = "block";

        // Prevent form submission
        event.preventDefault();
    } else {
        // Hide error message if everything is valid
        document.getElementById('errorMessage').style.display = "none";
    }
});
