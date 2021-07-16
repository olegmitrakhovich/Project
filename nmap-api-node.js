var express = require("express");
const spawn = require("child_process").execSync;
var app = express();
//var execSync = require('execSync');


app.get("/url", (req, res, next) => {

  var dataToSend;
  //spawn new child process to call the python script
  const python = spawn('python3', ['NmapProject.py 13.227.246.6']);
  //const python = execSync.run('python3', ['NmapProject.py 13.227.246.6']);
  // collect data from Script
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    dataToSend = data.toString();
  });
    //in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`);
      //send data to browser
      res.send(dataToSend)
    });

 //res.json(["Running Script!"]);
});

app.listen(3001, () => {
 console.log("Server running on port 3001");
});
