// This is where we'll store the Mad Libs data once we load the JSON
let madlibData = null;

// Fetch the JSON data
fetch('madlibs_input.json') // Path to your JSON file
  .then(response => response.json())
  .then(data => {
    madlibData = data; // Store the data in the madlibData variable
  })
  .catch(error => {
    console.error('Error loading the JSON file:', error);
  });

// Function to generate a Mad Lib
function generateMadLib() {
  if(!madlibData) {
    alert("Madlibs data not loaded!")
    return;
  }

  const templates = madlibData.templates
  const adjectives = madlibData.values.adjectives
  const nouns = madlibData.values.nouns
  const verbs = madlibData.values.verbs

  // get a random value from the templates array
  const template = templates[Math.floor(Math.random() * templates.length)]

  const story = template
  .replace(/{adjective}/g, adjectives[Math.floor(Math.random() * adjectives.length)])
  .replace(/{noun}/g, nouns[Math.floor(Math.random() * nouns.length)])
  .replace(/{verb}/g, verbs[Math.floor(Math.random() * verbs.length)]);

  document.getElementById('madlib-output').textContent = story;
}

// Add event listener to button
document.getElementById('generate-btn').addEventListener('click', generateMadLib);
