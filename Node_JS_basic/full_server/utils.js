const fs = require('fs');

const readDatabase = (filepath) => new Promise((resolve, reject) => {
  fs.readFile(filepath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = {};

    lines.slice(1).forEach((line) => {
      const [firstname, , , field] = line.split(',');

      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstname);
    });

    resolve(students);
  });
});

module.exports = readDatabase;
