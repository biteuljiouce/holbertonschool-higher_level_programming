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
document.querySelector('#toggle_header').addEventListener('click', toggleClass);
