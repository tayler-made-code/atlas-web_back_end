class AppController {
  // create a static method getHomepage. It accepts request and response
  // and returns a 200 status and the message 'Hello Holberton School!'

  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!');
  }
}