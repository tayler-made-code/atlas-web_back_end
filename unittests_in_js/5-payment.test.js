const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment'); // Adjust the path as necessary

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('should log "The total is: 120" and be called once with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWith(consoleSpy, 'The total is: 120');
  });

  it('should log "The total is: 20" and be called once with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);

    sinon.assert.calledOnce(consoleSpy);
    sinon.assert.calledWith(consoleSpy, 'The total is: 20');
  });
});
