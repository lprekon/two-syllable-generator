
// Get the button element from the DOM
const button = document.getElementById('main-button');

// Get the output div element from the DOM
const outputP = document.getElementById('output');

// Add a click event listener to the button
let codas, nuclei, onsets;

Promise.all([
    fetch('/assets/codas.txt').then(response => response.text()),
    fetch('/assets/nuclei.txt').then(response => response.text()),
    fetch('/assets/onsets.txt').then(response => response.text())
])
    .then(([codasContent, nucleiContent, onsetsContent]) => {
        codas = codasContent.split(', ');
        nuclei = nucleiContent.split(', ');
        onsets = onsetsContent.split(', ');

        button.addEventListener('click', () => {

            let newContent = '';
            for (let i = 0; i < 2; i++) {
                var mode = Math.floor(Math.random() * 3);
                const randomCoda = codas[Math.floor(Math.random() * codas.length)];
                const randomNucleus = nuclei[Math.floor(Math.random() * nuclei.length)];
                const randomOnset = onsets[Math.floor(Math.random() * onsets.length)];
                if (mode === 0) {
                    newContent += randomOnset + randomNucleus;
                }
                else if (mode === 1) {
                    newContent += randomNucleus + randomCoda;
                }
                else if (mode === 2) {
                    newContent += randomOnset + randomNucleus + randomCoda;
                }
                else {
                    newContent = "Error: mode not found."
                }
            }

            outputP.textContent = newContent;
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

