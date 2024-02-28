// The first one is getAllStudents:
// The method accepts request and response as argument
// It should return a status 200
// It calls the function readDatabase from the utils file, and display in the page:
// First line: This is the list of our students
// And for each field (order by alphabetic order case insensitive), a line that displays the number of students in the field, and the list of first names (ordered by appearance in the database file) with the following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
// If the database is not available, it should return a status 500 and the error message Cannot load the database

// The second one is getAllStudentsByMajor:
// The method accepts request and response as argument
// It should return a status 200
// It uses a parameter that the user can pass to the browser major. The major can only be CS or SWE. If the user is passing another parameter, the server should return a 500 and the error Major parameter must be CS or SWE
// It calls the function readDatabase from the utils file, and display in the page the list of first names for the students (ordered by appearance in the database file) in the specified field List: LIST_OF_FIRSTNAMES_IN_THE_FIELD
// If the database is not available, it should return a status 500 and the error message Cannot load the database
const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((fields) => {
        let students = '';
        for (const field in fields) {
          students += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        }
        response.status(200).send(`This is the list of our students\n${students}`);
      })
      .catch((err) => response.status(500).send(`Cannot load the database\n${err.message}`));
  }

  static getAllStudentsByMajor(request, response) {
    if (request.params.major !== 'CS' && request.params.major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
    } else {
      readDatabase(process.argv[2])
        .then((fields) => {
          response.status(200).send(`List: ${fields[request.params.major].join(', ')}`);
        })
        .catch((err) => response.status(500).send(`Cannot load the database\n${err.message}`));
    }
  }
}
