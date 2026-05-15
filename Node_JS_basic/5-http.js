const http = require("http");

const countStudents = require("./3-read_file_async");

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  if (req.url === "/") {
    res.end("Hello Holberton School!");
  } else if (req.url === "/students") {
    res.end("This is the list of our students");
    countStudents("database.csv")
      .then(() => {})
      .catch((err) => {
        console.error(err.message);
      });
  }
});

app.listen(1245);
module.exports = app;
