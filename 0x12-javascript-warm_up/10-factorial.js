#!/usr/bin/node


function factorial(num) {
  if (isNaN(num) || num === 0) {
	return 1;
  }
  return num * factorial(num - 1);
}

const arg = process.argv[2];

const number = parseInt(arg);

const result = factorial(number);
console.log(result);
