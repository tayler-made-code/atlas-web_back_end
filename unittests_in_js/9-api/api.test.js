const request = require('request');
const expect = require('chai').expect;

const baseUrl = 'http://localhost:7865';

describe('Index page', () => {
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
});

describe('Cart page', () => {
  it('should return the correct status code when id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
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