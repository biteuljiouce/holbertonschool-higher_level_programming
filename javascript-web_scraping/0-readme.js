#!/usr/bin/node

/*
// print process.argv
process.argv.forEach(function (val, index, array) {
	console.log(index + ': ' + val);
});
*/

// Include fs module
fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function(err, data) {
  if (err) {
	console.log(err);
  	}
	else
  console.log(data);
});
