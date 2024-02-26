const http = require('http');
const fs = require('fs').promises;

async function countStudents(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    const lines = data.split('\n');
    const usedLines = lines.filter((line) => line.length > 0);
    const students = usedLines.slice(1);

    const fields = {};
    for (const student of students) {
      const field = student.split(',')[3];
      if (fields[field]) {
        fields[field].push(student.split(',')[0]);
      } else {
        fields[field] = [student.split(',')[0]];
      }
    }

    let response = 'This is the list of our students\n';
    response += `Number of students: ${students.length}\n`;
    for (const field in fields) {
      if (field) {
        response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      }
    }

    // remove /n from the end of the string
    response = response.slice(0, -1);

    return response;
  } catch (error) {
    console.error('Error reading file:', error);
    return 'Error reading file';
  }
}

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students') {
    const filePath = process.argv[2];
    if (!filePath) {
      res.write('Error: No file path provided. Run the script with the CSV file path as an argument (e.g. node 5-http.js database.csv`)');
      res.end();
      return;
    }

    const studentsInfo = await countStudents(filePath);
    res.write(studentsInfo);
    res.end();
  } else {
    res.write('Not found');
    res.end();
  }
});

app.listen(1245);

module.exports = app;
