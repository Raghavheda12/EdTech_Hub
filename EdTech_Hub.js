// Function to validate and handle form submission
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("contactForm").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form from submitting automatically

        let name = document.getElementById("name").value.trim();
        let email = document.getElementById("email").value.trim();
        let phone = document.getElementById("phone").value.trim();
        let message = document.getElementById("message").value.trim();

        if (name === "" || email === "") {
            alert("Please fill in all required fields (Name & Email).");
            return;
        }

        if (!validateEmail(email)) {
            alert("Please enter a valid email address.");
            return;
        }

        if (phone !== "" && !validatePhone(phone)) {
            alert("Please enter a valid 10-digit phone number.");
            return;
        }

        alert("Form submitted successfully!");
        document.getElementById("contactForm").reset(); // Clear form fields
    });

    function validateEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    function validatePhone(phone) {
        return /^[0-9]{10}$/.test(phone);
    }
});
