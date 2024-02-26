const fs = require('fs').promises;
const path = require('path');

function countStudents(filePath) {
  // Function that counts the number of students in a database
  // and logs them to the console
  const fullPath = path.resolve(filePath);

  return new Promise((resolve, reject) => {
    fs.readFile(fullPath, 'utf-8')
      .then((data) => {
        // Split the data by lines
        const lines = data.split('\n');

        // Remove any empty lines
        const usedLines = lines.filter((line) => line.length > 0);

        // Remove header
        const students = usedLines.slice(1);

        // Log the number of students
        console.log(`Number of students: ${students.length}`);

        // Log the number of students in each field
        const fields = {};
        for (const student of students) {
          const field = student.split(',')[3];
          if (fields[field]) {
            fields[field].push(student.split(',')[0]);
          } else {
            fields[field] = [student.split(',')[0]];
          }
        }
        for (const field in fields) {
          if (field) {
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
          }
        }
        resolve();
      })
      .catch(() => {
        reject(Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
