const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Remove the first line - header
      lines.shift();

      const students = {};
      let totalStudents = 0;

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!firstname || !field) {
          return;
        }

        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
        totalStudents += 1;
      });

      // Save the total students to console log
      console.log(`Number of students: ${totalStudents}`);

      // Save each field with the number of students
      for (const field in students) {
        if (Object.prototype.hasOwnProperty.call(students, field)) {
          const studentList = students[field];
          console.log(
            `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`,
          );
        }
      }

      resolve();
    });
  });
}

module.exports = countStudents;
