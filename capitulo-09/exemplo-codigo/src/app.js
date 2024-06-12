const express = require('express');
const app = express();

app.use(express.json());

app.use('/', (req, res) => {
    res.send('Hello, world!');
});

const itemRoutes = require('./routes/itemRoutes');
app.use('/items', itemRoutes);

module.exports = app;