function changeColor(event) {
	document.querySelector('header').style.color = 'red';
}
document.querySelector('#red_header').addEventListener('click', changeColor);
