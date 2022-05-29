const bcrypt = require("bcrypt");

module.exports = async (req, res) => {
  const hash = bcrypt.hashSync(req.body.password, 10);
  var blogpost = "";
  var sql = `INSERT INTO users (username, password,email) VALUES (?,?,?)`;
  db.query(
    sql,
    [req.body.username, hash, req.body.email],
    function (err, result) {
      if (err) throw err;
      console.log(result.affectedRows);
    }
  );

  var sql = `select * from users where username=?`;
  db.query(sql, [req.body.username], function (err, result, fields) {
    if (err) throw err;
    console.log(result);
    blogpost = {
      username: result[0].username,
      email: result[0].email,
    };
  });

  res.render("data", {
    blogpost,
  });
};
