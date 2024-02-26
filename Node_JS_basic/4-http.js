// create a small server using http module
var http = require('http');
// Displays Hello Holberton School! in the page body for any endpoint as plain text

// the server should be assigned to the variable app
var app = http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  // Displays Hello Holberton School! in the page body
  res.write('Hello Holberton School!');
  res.end();
});
// HTTP server should listen on port 1245
app.listen(1245);
