// create a new module named Utils
// create a property named calculateNumber

module.exports = {
  calculateNumber: function(type, a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    if (type === 'SUM') {
      return roundedA + roundedB;
    }

    if (type === 'SUBTRACT') {
      return roundedA - roundedB;
    }

    if (type === 'DIVIDE' && roundedB !== 0) {
      return roundedA / roundedB;
    } else if (roundedB === 0) {
      return('Error');
    }

    return("Invalid type of operation. Please use SUM, SUBTRACT or DIVIDE.")
  }
}
