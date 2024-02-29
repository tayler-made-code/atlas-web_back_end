import express from 'express';
const route = require('./routes/index');

const app = express();

app.use(route);

app.listen(1245);

export default app;
