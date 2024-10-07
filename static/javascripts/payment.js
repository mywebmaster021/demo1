   // Function to open the popup
   document.getElementById("continue-button").onclick = function() {
    document.getElementById("popup").style.display = "block"; // Show the popup
}

// Function to close the popup
document.getElementById("closePopup").onclick = function() {
    document.getElementById("popup").style.display = "none"; // Hide the popup
}

// Close the popup if the user clicks anywhere outside of it
window.onclick = function(event) {
    const popup = document.getElementById("popup");
    if (event.target === popup) {
        popup.style.display = "none"; // Hide the popup
    }
}