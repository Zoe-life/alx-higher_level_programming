#!/usr/bin/node

function findSecondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }
  const numbers = args.map(arg => parseInt(arg));
  numbers.sort((a, b) => b - a);
  const uniqueNumbers = [...new Set(numbers)];
  return uniqueNumbers[1] || 0;
}

const args = process.argv.slice(2);

const secondBiggest = findSecondBiggest(args);

console.log(secondBiggest);
