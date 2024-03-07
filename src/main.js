
// Get the button element from the DOM
const button = document.getElementById('main-button');

// Get the output div element from the DOM
const outputP = document.getElementById('output');

// Add a click event listener to the button

fetch('/assets/syllable_list.txt')
    .then(response => response.text())
    .then(content => {
        const syllableList = content.split('\n');
        button.addEventListener('click', () => {
            // Randomly pick two lines from the syllable list
            const randomLine1 = syllableList[Math.floor(Math.random() * syllableList.length)];
            console.log('randomLine1', randomLine1);
            const randomLine2 = syllableList[Math.floor(Math.random() * syllableList.length)];
            console.log('randomLine2', randomLine2);

            // Concatenate the two lines
            const newContent = randomLine1 + "-" + randomLine2;

            // Set the content of the output div
            outputP.textContent = newContent;
        });
    })
    .catch(error => {
        console.error('Error fetching syllable list:', error);
    });