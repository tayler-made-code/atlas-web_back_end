const express = require('express');
const app = express();
const port = 7865;

// Define route for the root URL '/'
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Start the server and listen on the specified port
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});
