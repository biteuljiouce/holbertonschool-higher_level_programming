/*
Write a JavaScript script that fetches and lists the title for all movies by using this URL:
https://swapi-api.hbtn.io/api/films/?format=json

All movie titles must be list in the HTML ul element with id list_movies
You must use the Fetch API.
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

function addMovie(json) {
	i = 0;
	while (json.results[i] != null) {
		li = document.querySelector('#list_movies').appendChild(document.createElement("li"));
		li.textContent = json.results[i].title;
		i++;
	}
}

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    return response.json();
  })
  .then((json) => addMovie(json))
  .catch((err) => console.error(`Fetch problem: ${err.message}`));
