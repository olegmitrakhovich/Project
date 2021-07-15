var express = require("express");
var app = express();


app.get("/url", (req, res, next) => {

 res.json(["Running Script!"]);
});

app.listen(3001, () => {
 console.log("Server running on port 3001");
});
