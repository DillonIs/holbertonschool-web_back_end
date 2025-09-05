const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file - synchronously
    const data = fs.readFileSync(path, 'utf-8');

    // Filter empty lines after splitting the file content
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Identify if there are any lines in the file besides the header
    if (lines.length < 2) {
      throw new Error('Cannot load the database');
    }

    // Remove the header - first line
    const students = lines.slice(1);

    // Variables for counting
    const totalStudents = students.length;
    const fields = {};

    students.forEach((line) => {
      // Ignore lastname and age
      const [firstname, , , field] = line.split(',');

      if (!Object.prototype.hasOwnProperty.call(fields, field)) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    // Display the total number of students
    console.log(`Number of students: ${totalStudents}`);

    // Display the count by field
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        const studentsInField = fields[field];
        console.log(`Number of students in ${field}: ${studentsInField.length}. List: ${studentsInField.join(', ')}`);
      }
    }
  } catch (error) {
    // Throw an error when the file can't be loaded
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
