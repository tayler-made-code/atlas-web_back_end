// recreate the small HTTP server using Express:

// It should be assigned to the variable app and this one must be exported
// HTTP server should listen on port 1245
// It should return plain text
// When the URL path is /, it should display Hello Holberton School! in the page body
// When the URL path is /students, it should display This is the list of our students
// followed by the same content as the file 3-read_file_async.js (with and without the database)
// the name of the database must be passed as argument of the file
// CSV file can contain empty lines (at the end) - and they are not a valid student!

const express = require('express');
const fs = require('fs').promises;
const path = require('path');

const app = express();

async function countStudents(filePath) {
  console.log('starting countStudents');
  const fullPath = path.resolve(filePath);
  try {
    const data = await fs.readFile(fullPath, 'utf-8');
    const lines = data.split('\n');
    const usedLines = lines.filter((line) => line.length > 0);
    const students = usedLines.slice(1);

    let studentInfo = `Number of students: ${students.length}\n`;

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
        studentInfo += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      }
    }
    // remove /n from the end of the string
    studentInfo = studentInfo.slice(0, -1);

    return studentInfo;
  } catch (error) {
    throw Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    console.log('starting /students');
    const outputMessage = 'This is the list of our students\n';
    const studentInfo = await countStudents(process.argv[2]);
    res.send(`${outputMessage}${studentInfo}`);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.listen(1245);

module.exports = app;
