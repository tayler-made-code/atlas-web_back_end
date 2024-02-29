import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase('process.argv[2]')
      .then(data => {
        let responseText = 'This is the list of our students\n';
        
        // Get the fields in alphabetical order
        const fields = Object.keys(data).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
        
        fields.forEach(field => {
          const firstNames = data[field].join(', ');
          responseText += `Number of students in ${field}: ${data[field].length}. List: ${firstNames}\n`;
        });
        
        // Send the response
        res.status(200).send(responseText);
      })
      .catch(error => {
        console.error(error);
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.query; // Extract the 'major' query parameter

    // Validate the 'major' parameter
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    readDatabase('process.argv[2]')
      .then(data => {
        // Check if the major exists in the database
        if (!data[major]) {
          return res.status(500).send('Major not found in the database');
        }

        const firstNames = data[major].join(', ');
        const responseText = `List: ${firstNames}`;

        // Send the response
        res.status(200).send(responseText);
      })
      .catch(error => {
        console.error(error);
        res.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
