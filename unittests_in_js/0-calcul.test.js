// You can assume a and b are always number
// Tests should be around the “rounded” part

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return the sum of two numbers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return the sum of two numbers, with the first rounded up', () => {
    assert.strictEqual(calculateNumber(1.6, 3), 5);
  });

  it('should return the sum of two numbers, with the first rounded down', () => {
    assert.strictEqual(calculateNumber(1.3, 3), 4);
  });

  it('should return the sum of two numbers, with the second rounded up', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return the sum of two numbers, with the second rounded down', () => {
    assert.strictEqual(calculateNumber(1, 3.3), 4);
  });

  it('should return the sum of two numbers rounded down', () => {
    assert.strictEqual(calculateNumber(1.3, 3.4), 4);
  });

  it('should return the sum of two numbers rounded up', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should return the sum of two numbers rounded down and up', () => {
    assert.strictEqual(calculateNumber(1.3, 3.7), 5);
  });

  it('should return the sum of two numbers rounded up and down', () => {
    assert.strictEqual(calculateNumber(1.5, 3.3), 5);
  });
});