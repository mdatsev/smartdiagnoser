const express = require('express');
const app = express();
const pgp = require('pg-promise')()
const db = pgp('postgres:/postgres:12345@localhost:5432/postgres')
const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({
    extended: true
}));
app.set('view engine', 'pug');
app.listen(3000, function () {
    console.log('Ready!');
});
app.use(express.static('public'));
app.get('/', function (req, res) {
    res.render('index');
});
app.post('/upload', function (req, res) {
    console.log(req.body);
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["../models/liver.py", 2, 2]);

    process.stdout.on('data', function (data) {
        console.log(data.toString())
    });

    process.stderr.on('data', function (data) {
        console.log(data.toString())
    });
})

