/*
Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

The name must be displayed in the HTML tag with id character.
You must use the Fetch API.
You probably should read something about usign Promises later.
*/

function changeColor(event) {
	document.querySelector('header').style.color = 'red';
}
function addRedClass(event) {
	document.querySelector('header').className = 'red';
}
function toggleClass(event) {
	currentClass = document.querySelector('header').className;
	if (currentClass == 'red')
		document.querySelector('header').className = 'green';
	else
		document.querySelector('header').className = 'red';
}
function addItem(event) {
	li = document.querySelector('ul.my_list').appendChild(document.createElement("li"));
	li.textContent = 'item';
}
function updateHeaderText(event) {
	document.querySelector('header').textContent = 'New Header !!!';
}

function displayName(json) {
	document.querySelector('#character').textContent = json.name;
}

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    return response.json();
  })
  .then((json) => displayName(json))
  .catch((err) => console.error(`Fetch problem: ${err.message}`));
