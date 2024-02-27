const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with correct arguments', () => {
    // Stub Utils.calculateNumber to always return 10
    let stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // spy on console.log to verify the messae logged
    let consoleSpy = sinon.spy(console, 'log');

    //Call the function under test
    sendPaymentRequestToApi(100, 20);

    // Verify that Utils.calculateNumber was called with the correct arguments
    sinon.assert.calledWith(stub, 'SUM', 100, 20);

    // Verify that console.log was called with the correct message
    sinon.assert.calledWith(consoleSpy, 'The total is: 10');

    // Restore the original function
    stub.restore();
    consoleSpy.restore();
  });
});
