const express = require('express');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const DATABASE = args[0];

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const response = 'This is the list of our students\n';
  try {
    const students = await countStudents(DATABASE);
    res.send(`${response}${students.join('\n')}`);
  } catch (error) {
    res.send(`${response}${error.message}`);
  }
});

app.listen(port, () => {
  console.log(`Express server is listening on port ${port}`);
});

module.exports = app;
