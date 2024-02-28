const express = require('express');
const app = express();
const port = 7865;

// Define route for the root URL '/'
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Define route for the /available_payments endpoint
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

// Define route for the /login endpoint
app.post('/login', express.json(), (req, res) => {
  const username = req.query.userName;
  res.send(`Welcome ${username}`);
});

// Start the server and listen on the specified port
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

app.get('/cart/:id(\\d+)', (req, res) => {
  let cartId = req.params.id;
  res.send(`Payment methods for cart ${cartId}`);
});

module.exports = app;
