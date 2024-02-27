// You can assume a and b are always number

const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('should return the sum of two numbers', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
  });

  it('should return the sum of two numbers, with the first rounded up', () => {
    assert.strictEqual(calculateNumber('SUM', 1.6, 3), 5);
  });

  it('should return the sum of two numbers, with the first rounded down', () => {
    assert.strictEqual(calculateNumber('SUM', 1.3, 3), 4);
  });

  it('should return the sum of two numbers, with the second rounded up', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
  });

  it('should return the sum of two numbers, with the second rounded down', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3.3), 4);
  });

  it('should return the sum of two numbers rounded down', () => {
    assert.strictEqual(calculateNumber('SUM', 1.3, 3.4), 4);
  });

  it('should return the sum of two numbers rounded up', () => {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
  });

  it('should return the sum of two numbers rounded down and up', () => {
    assert.strictEqual(calculateNumber('SUM', 1.3, 3.7), 5);
  });

  it('should return the sum of two numbers rounded up and down', () => {
    assert.strictEqual(calculateNumber('SUM', 1.5, 3.3), 5);
  });

  it('should return the difference of two numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), -2);
  });

  it('should return the difference of two numbers, with the first rounded up', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.6, 3), -1);
  });

  it('should return the difference of two numbers, with the first rounded down', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.3, 3), -2);
  });

  it('should return the difference of two numbers, with the second rounded up', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });

  it('should return the difference of two numbers, with the second rounded down', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 3.3), -2);
  });

  it('should return the difference of two numbers rounded down', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.3, 3.4), -2);
  });

  it('should return the difference of two numbers rounded up', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
  });

  it('should return the difference of two numbers rounded down and up', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.3, 3.7), -3);
  });

  it('should return the difference of two numbers rounded up and down', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.3), -1);
  });

  it('should return the division of two numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 4, 1), 4);
  });

  it('should return the division of two numbers, with the first rounded up', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.6, 4), .5);
  });

  it('should return the division of two numbers, with the first rounded down', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3.3, 1), 3);
  });

  it('should return the division of two numbers, with the second rounded up', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 3.7), .25);
  });

  it('should return the division of two numbers, with the second rounded down', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3, 1.3), 3);
  });

  it('should return the division of two numbers rounded down', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3.4, 1.3), 3);
  });

  it('should return the division of two numbers rounded up', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3.7, 1.5), 2);
  });

  it('should return the division of two numbers rounded down and up', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3.4, 2.7), 1);
  });

  it('should return the division of two numbers rounded up and down', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 2.5, 3.3), 1);
  });

  it('should return an error message when dividing by 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
});