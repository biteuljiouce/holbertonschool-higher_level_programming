function changeColor(event) {
	document.querySelector('header').style.color = 'red';
}
function addRedClass(event) {
	document.querySelector('header').className = 'red';
}
document.querySelector('#red_header').addEventListener('click', addRedClass);
