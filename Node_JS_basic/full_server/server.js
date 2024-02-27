// Inside the file named full_server/server.js, create a small Express server:

// It should use the routes defined in full_server/routes/index.js
// It should use the port 1245

const express = require('express');
const router = require('./routes/index');

const app = express();
const port = 1245;

app.use('/', router);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

module.exports = app;
