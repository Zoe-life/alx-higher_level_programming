#!/usr/bin/node

const arg = process.argv[2];


let numOccurrences;


try {
  numOccurrences = parseInt(arg);
} catch (error) {
  numOccurrences = NaN;
}

if (isNaN(numOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOccurrences; i++) {
	console.log('C is fun');
	}
}
