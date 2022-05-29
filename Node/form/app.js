const express = require("express");
const app = express();
const ejs = require("ejs");
const bodyParser = require("body-parser");
const homeC = require("./controllers/home");
const data = require("./controllers/data");
const createData = require("./controllers/create");
global.db = require("./models/dbconfig");
app.set("view engine", "ejs");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.get("/", homeC);
app.post("/data", data);
app.listen(3000, () => {
  console.log("App listening");
});
