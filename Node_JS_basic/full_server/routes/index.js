// import the AppController and StudentController
import AppController from '../controllers/AppController';
import StudentController from '../controllers/StudentController';

// Import Express
const express = require('express');

// Create an Express application
const app = express();

// Use the router
const router = express.Router();

// define route for the homepage
router.get('/', AppController.getHomepage);

// define route for the students
router.get('/students', StudentController.getAllStudents);

// define router for studetns by major
router.get('/students/:major', StudentController.getAllStudentsByMajor);

// Export the router
module.exports = router;
