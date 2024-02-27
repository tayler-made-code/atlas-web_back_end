// You can assume a and b are always number

const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai');

describe ('calculateNumber', () => {
  it('should return the sum of two numbers', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });

  it('should return the sum of two numbers, with the first rounded up', () => {
    expect(calculateNumber('SUM', 1.6, 3)).to.equal(5);
  });

  it('should return the sum of two numbers, with the first rounded down', () => {
    expect(calculateNumber('SUM', 1.3, 3)).to.equal(4);
  });

  it('should return the sum of two numbers, with the second rounded up', () => {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });

  it('should return the sum of two numbers, with the second rounded down', () => {
    expect(calculateNumber('SUM', 1, 3.3)).to.equal(4);
  });

  it('should return the sum of two numbers rounded down', () => {
    expect(calculateNumber('SUM', 1.3, 3.4)).to.equal(4);
  });

  it('should return the sum of two numbers rounded up', () => {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });

  it('should return the sum of two numbers rounded down and up', () => {
    expect(calculateNumber('SUM', 1.3, 3.7)).to.equal(5);
  });

  it('should return the sum of two numbers rounded up and down', () => {
    expect(calculateNumber('SUM', 1.5, 3.3)).to.equal(5);
  });

  it('should return the difference of two numbers', () => {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
  });

  it('should return the difference of two numbers, with the first rounded up', () => {
    expect(calculateNumber('SUBTRACT', 1.6, 3)).to.equal(-1);
  });

  it('should return the difference of two numbers, with the first rounded down', () => {
    expect(calculateNumber('SUBTRACT', 1.3, 3)).to.equal(-2);
  });

  it('should return the difference of two numbers, with the second rounded up', () => {
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
  });

  it('should return the difference of two numbers, with the second rounded down', () => {
    expect(calculateNumber('SUBTRACT', 1, 3.3)).to.equal(-2);
  });

  it('should return the difference of two numbers rounded down', () => {
    expect(calculateNumber('SUBTRACT', 1.3, 3.4)).to.equal(-2);
  });

  it('should return the difference of two numbers rounded up', () => {
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
  });

  it('should return the difference of two numbers rounded down and up', () => {
    expect(calculateNumber('SUBTRACT', 1.3, 3.7)).to.equal(-3);
  });

  it('should return the difference of two numbers rounded up and down', () => {
    expect(calculateNumber('SUBTRACT', 1.5, 3.3)).to.equal(-1);
  });

  it('should return the division of two numbers', () => {
    expect(calculateNumber('DIVIDE', 4, 1)).to.equal(4);
  });

  it('should return the division of two numbers, with the first rounded up', () => {
    expect(calculateNumber('DIVIDE', 1.6, 4)).to.equal(.5);
  });

  it('should return the division of two numbers, with the first rounded down', () => {
    expect(calculateNumber('DIVIDE', 3.3, 1)).to.equal(3);
  });

  it('should return the division of two numbers, with the second rounded up', () => {
    expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal(.25);
  });

  it('should return the division of two numbers, with the second rounded down', () => {
    expect(calculateNumber('DIVIDE', 3, 1.3)).to.equal(3);
  });

  it('should return the division of two numbers rounded down', () => {
    expect(calculateNumber('DIVIDE', 3.4, 1.3)).to.equal(3);
  });

  it('should return the division of two numbers rounded up', () => {
    expect(calculateNumber('DIVIDE', 3.7, 1.5)).to.equal(2);
  });

  it('should return the division of two numbers rounded down and up', () => {
    expect(calculateNumber('DIVIDE', 3.4, 2.7)).to.equal(1);
  });

  it('should return the division of two numbers rounded up and down', () => {
    expect(calculateNumber('DIVIDE', 2.5, 3.3)).to.equal(1);
  });

  it('should return an error message when dividing by 0', () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
  });
});