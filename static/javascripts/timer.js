let totalTime = getRandomTime(240, 360); // Random time between 4 minutes (240 seconds) and 6 minutes (360 seconds)
let innerBar = document.getElementById('innerBar');
let timeCount = document.getElementById('timeCount');

function getRandomTime(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min; // Generate random time between min and max
}

function updateTimer() {
    if (totalTime > 0) {
        totalTime--; // Decrease by 1 second

        // Update the inner bar width and display
        let percentage = (totalTime / (360)) * 100; // Use 360 for percentage calculation
        innerBar.style.width = percentage + '%';
        timeCount.innerText = formatTime(totalTime); // Update the displayed time inside the bar
    } else {
        clearInterval(timerInterval); // Stop the timer when it reaches 0
        setTimeout(resetTimer, 1000); // Reset after 1 second
    }
}

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
}

function resetTimer() {
    totalTime = getRandomTime(240, 360); // Reset to a new random time
    innerBar.style.width = '100%'; // Reset inner bar width
    timeCount.innerText = formatTime(totalTime); // Reset displayed time
    startTimer();
}

function startTimer() {
    timerInterval = setInterval(updateTimer, 1000); // Update every second
    timeCount.innerText = formatTime(totalTime); // Display initial time
}

// Start the timer
startTimer();