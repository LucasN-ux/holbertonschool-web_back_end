const http = require("http");

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  if (req.url === "/") {
    res.setHeader("Content-Type", "text/plain");
    res.end("Hello Holberton School!");
  } else if (req.url === "/students") {
    res.setHeader("Content-Type", "text/plain");
    res.end("This is the list of our students");
    const countStudents = require("./3-read_file_async");
    countStudents("database.csv")
      .then(() => {
      })
      .catch((err) => {
        console.error(err.message);
      });
  }
});

app.listen(1245);
module.exports = app;
