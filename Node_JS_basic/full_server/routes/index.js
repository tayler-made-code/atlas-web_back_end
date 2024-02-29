// import the AppController and StudentController
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

// Import Express
const express = require('express');

// Use the router
const router = express.Router();

// define route for the homepage
router.get('/', AppController.getHomepage);

// define route for the students
router.get('/students', StudentsController.getAllStudents);

// define router for studetns by major
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

// Export the router
module.exports = router;
