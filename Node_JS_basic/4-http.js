const http = require('http');

const app = http.createServer((req, res) => {
  // Set the response header
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send the response body
  res.end('Hello Holberton School!');
});

const port = 1245;

app.listen(port, () => {
  console.log(`Server is listening on ${port}`);
});

module.exports = app;
