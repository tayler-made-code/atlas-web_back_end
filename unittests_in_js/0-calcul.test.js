// You can assume a and b are always number
// Tests should be around the “rounded” part

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return the sum of two numbers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return the sum of two numbers, with the first rounded', () => {
    assert.strictEqual(calculateNumber(1.3, 3), 4);
  });

  it('should return the sum of two numbers, with the second rounded', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return the sum of two rounded numbers', () => {
    assert.strictEqual(calculateNumber(1.3, 3.7), 5);
  });
});