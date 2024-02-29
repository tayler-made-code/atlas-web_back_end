class AppController {
  static getHomepage(req, res) {
    // Send a 200 status code and the message "Hello Holberton School!"
    res.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
