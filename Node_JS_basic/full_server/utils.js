const fs = require('fs');

function readDatabase(filePath) {
  // It should read the database asynchronously
  // It should return a promise
  // When the file is not accessible, it should reject the promise with the error
  // When the file can be read, it should return an object of arrays of the firstname of students per fields

  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      } else {
        const students = JSON.parse(data);
        const fields = {};
        for (const field in students) {
          fields[field] = students[field].map((student) => student.firstname);
        }
        resolve(fields);
      }
    });
  });
}

module.exports = readDatabase;
