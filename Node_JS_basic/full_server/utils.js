const fs = require('fs').promises;

async function readDatabase(filePath) {
  try {
    // Read the file asynchronously
    const data = await fs.readFile(filePath, 'utf8');
    
    // Parse the file content assuming it's JSON
    const students = JSON.parse(data);
    
    // Transform the data into the desired format: an object of arrays of first names per field
    const result = students.reduce((acc, student) => {
      // Assuming each student object has a 'field' and 'firstName' property
      const { field, firstName } = student;
      
      // Initialize the array for the field if it doesn't exist
      if (!acc[field]) {
        acc[field] = [];
      }
      
      // Add the student's first name to the array for their field
      acc[field].push(firstName);
      
      return acc;
    }, {});
    
    // Return the transformed data
    return result;
  } catch (error) {
    // Reject the promise with the error if the file is not accessible
    throw error;
  }
}

module.exports = readDatabase;
