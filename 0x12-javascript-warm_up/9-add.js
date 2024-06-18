#!/usr/bin/node


function add(a, b) {
  const numA = parseInt(a, 10);
  const numB = parseInt(b, 10);

  if (isNaN(numA) || isNaN(numB)) {
	return "Invalid arguments";
  }
  return numA + numB;
}

const firstArg = process.argv[2];
const secondArg = process.argv[3];

const sum = add(firstArg, secondArg);

console.log(sum);
