const express = require("express");
const app = new express();
const ejs = require("ejs");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const fileUpload = require("express-fileupload");
const newPostController = require("./controllers/newPost");
const homeController = require("./controllers/home");
const storePostController = require("./controllers/storePost");
const getPostController = require("./controllers/getPost");
const validateMiddleware = require("./middleware/validationMiddleware");
const newUserController = require("./controllers/newUser");
const storeUserController = require("./controllers/storeUser");
const loginController = require("./controllers/login");
const loginUserController = require("./controllers/loginUser");
const expressSession = require("express-session");
const authMiddleware = require("./middleware/authMiddleware");
mongoose.connect("mongodb://localhost/my_database", { useNewUrlParser: true });
app.use(
  expressSession({
    secret: "keyboard cat",
  })
);
app.set("view engine", "ejs");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.use(fileUpload());
app.post("/users/register", storeUserController);
app.get("/auth/login", loginController);
app.post("/users/login", loginUserController);
app.post("/posts/store", authMiddleware, storePostController);
app.use("/posts/store", validateMiddleware);
app.get("/", homeController);
app.get("/auth/register", newUserController);
app.get("/post/:id", getPostController);
app.get("/posts/new", authMiddleware, newPostController);

app.listen(4000, () => {
  console.log("App listening on port 4000");
});
