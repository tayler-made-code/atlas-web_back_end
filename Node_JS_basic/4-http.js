// create a small server using http module
var http = require('http');
// Displays Hello Holberton School! in the page body for any endpoint as plain text

// the server should be assigned to the variable app
var app = http.createServer(function (req, res) {
  // Displays Hello Holberton School! in the page body
  res.write('Hello Holberton School!');
  res.end();
}).listen(1245); // HTTP server should listen on port 1245

module.exports = app;
