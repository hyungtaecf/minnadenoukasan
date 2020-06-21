const prev = document.querySelector('#prev');
const next = document.querySelector('#next');
var els = document.querySelectorAll("[type='radio']");

const changingInterval = 5000; //milliseconds
var timeToNextPicture = Date.now() + changingInterval;

var displayingItemsNumber = 7 // IMPORTANT: Should be the same as in Gallery's views.py
var fromIndex = 0
var toIndex = displayingItemsNumber


function simulateClick(id) {
    var evt = document.createEvent("MouseEvents");
    evt.initMouseEvent("click", true, true, window, 1, 0, 0, 0, 0,
        false, false, false, false, 0, null);

    var cb = document.getElementById(id);
    cb.dispatchEvent(evt);
}

function autoPressNext() {
    return new Promise(resolve => {
        setTimeout(() => {
            if (Date.now() > timeToNextPicture) simulateClick('next')
            resolve();
        }, 2000);
    });
}

async function asyncCall() {
    while (true) {
        await autoPressNext();
    }
}

asyncCall();
initialize();

// main logic
function initialize() {
    els = document.querySelectorAll("[type='radio']");
    for (const el of els)
        el.addEventListener("input", e => reorder(e.target, els));
    reorder(els[0], els);
}

function reorder(targetEl, els) {
    const nItems = els.length;
    let processedUncheck = 0;
    for (const el of els) {
        const containerEl = el.nextElementSibling;
        if (el === targetEl) { //checked radio
            containerEl.style.setProperty("--w", "100%");
            containerEl.style.setProperty("--l", "0");
        } else { //unchecked radios
            containerEl.style.setProperty("--w", `${100/(nItems-1)}%`);
            containerEl.style.setProperty("--l", `${processedUncheck * 100/(nItems-1)}%`);
            processedUncheck += 1;
        }
    }
    timeToNextPicture = Date.now() + changingInterval;
}

// IMPORTANT: This script is partial. The functionality continues in the index.html page