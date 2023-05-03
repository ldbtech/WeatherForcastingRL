const flightElements = document.querySelectorAll('.flight');
const flightStatusElements = document.querySelectorAll('.flight-status');

function takeOff(flightNumber) {
  flightElements[flightNumber].style.transform = 'translateX(100%)';
  flightStatusElements[flightNumber].textContent = 'Taking off...';
}

function land(flightNumber) {
  flightElements[flightNumber].style.transform = 'translateX(0)';
  flightStatusElements[flightNumber].textContent = 'Landing...';
}

function delay(flightNumber) {
  flightStatusElements[flightNumber].textContent = 'Delayed';
  flightStatusElements[flightNumber].classList.add('delayed');
}

function redirect(flightNumber) {
  flightStatusElements[flightNumber].textContent = 'Redirected';
  flightStatusElements[flightNumber].classList.add('delayed');
}

setTimeout(() => takeOff(0), 2000);
setTimeout(() => land(0), 8000);
setTimeout(() => delay(0), 12000);
setTimeout(() => redirect(0), 16000);

setTimeout(() => takeOff(1), 5000);
setTimeout(() => land(1), 11000);
setTimeout(() => delay(1), 15000);
setTimeout(() => redirect(1), 19000);
