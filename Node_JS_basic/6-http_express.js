// Create a small HTTP server using Express module

const express = require('express');

const app = express(); // It should be assigned to the variable app

// Displays "Hello Holberton School!" in the page body for the endpoint /
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// HTTP server should listen on port 1245
app.listen(1245);

module.exports = app;
