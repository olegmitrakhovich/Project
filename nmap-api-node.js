var express = require("express");
const exec = require("child_process").execSync;
var app = express();
//var execSync = require('execSync');


app.get("/url", (req, res, next) => {

  var dataToSend = exec("python3 NmapProject.py 13.227.246.50");

  res.send(dataToSend.toString("utf8"));
 //res.json(["Running Script!"]);
});

app.listen(3001, () => {
 console.log("Server running on port 3001");
});
