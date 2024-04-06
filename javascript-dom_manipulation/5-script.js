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
document.querySelector('#update_header').addEventListener('click', updateHeaderText);
