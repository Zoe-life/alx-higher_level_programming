#!/usr/bin/node

exports.converter = function (base) {
  function convert (num) {
    const digits = '0123456789ABCDEF';

    let converted = '';
    while (num > 0) {
      const remainder = num % base;
      converted = digits[remainder] + converted;
      num = Math.floor(num / base);
    }
    return converted;
  }

  return function (num) {
    return convert(num);
  };
};
