var spawn = require("child_process").spawn;
var process = spawn('python', ["my_script.py", 2, 2]);

process.stdout.on('data', function (data) {
    console.log(data.toString())
});

process.stderr.on('data', function (data) {
    console.log(data.toString())
});