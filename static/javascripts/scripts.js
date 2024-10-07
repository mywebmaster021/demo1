const timerDisplay = document.getElementById("timer");
const timerDuration = 20 * 60 * 1000; // 20 minutes in milliseconds

// Set or get the global start time (either from localStorage or set a new one)
let globalStartTime = localStorage.getItem("globalStartTime");

if (!globalStartTime) {
    globalStartTime = new Date().getTime(); // Set current time as start time
    localStorage.setItem("globalStartTime", globalStartTime); // Save to localStorage
}

// Function to calculate remaining time from the global start time
function getRemainingTime() {
    const now = new Date().getTime(); // Get the current time
    const elapsed = now - globalStartTime; // Calculate the time elapsed since the timer started
    return timerDuration - (elapsed % timerDuration); // Remaining time in the current 20-minute interval
}

// Function to update the timer display
function updateTimerDisplay() {
    const timeRemaining = getRemainingTime(); // Calculate the remaining time

    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
    timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
}

// Start the timer immediately and update the display every second
function startTimer() {
    updateTimerDisplay(); // Update the timer display immediately on page load
    setInterval(updateTimerDisplay, 1000); // Update the timer display every second
}

startTimer(); // Start the countdown




let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.querySelectorAll('.slide');
  let dots = document.querySelectorAll('.dot');

  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}

  // Hide all slides
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }

  // Remove 'active' class from all dots
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(' active', '');
  }

  // Show the current slide and add 'active' class to the corresponding dot
  slides[slideIndex - 1].style.display = 'block';
  dots[slideIndex - 1].className += ' active';
}

// Automatic slide change every 5 seconds
setInterval(function() {
  plusSlides(1);
}, 2000);

//best of elctronics
const tabsBox = document.querySelector(".tabs-box"),
allTabs = tabsBox.querySelectorAll(".tab"),
arrowIcons = document.querySelectorAll(".icon i");

let isDragging = false;

const handleIcons = (scrollVal) => {
let maxScrollableWidth = tabsBox.scrollWidth - tabsBox.clientWidth;
arrowIcons[0].parentElement.style.display = scrollVal <= 0 ? "none" : "flex";
arrowIcons[1].parentElement.style.display = maxScrollableWidth - scrollVal <= 1 ? "none" : "flex";
}

arrowIcons.forEach(icon => {
icon.addEventListener("click", () => {
    let scrollWidth = tabsBox.scrollLeft += icon.id === "left" ? -340 : 340;
    handleIcons(scrollWidth);
});
});

const dragging = (e) => {
if(!isDragging) return;
tabsBox.classList.add("dragging");
tabsBox.scrollLeft -= e.movementX;
handleIcons(tabsBox.scrollLeft);
}

const dragStop = () => {
isDragging = false;
tabsBox.classList.remove("dragging");
}

tabsBox.addEventListener("mousedown", () => isDragging = true);
tabsBox.addEventListener("mousemove", dragging);
document.addEventListener("mouseup", dragStop);