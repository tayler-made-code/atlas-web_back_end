const request = require('request');
const expect = require('chai').expect;

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should return the correct status code', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should return the correct status code when id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct result when id is not a number', (done) => {
    request.get(`${baseUrl}/cart/anything`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});