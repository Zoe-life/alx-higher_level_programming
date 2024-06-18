#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const occurrence in dict) {
  const userId = dict[occurrence];

  if (newDict[occurrence]) {
    newDict[occurrence].push(userId);
  } else {
    newDict[occurrence] = [userId];
  }
}

console.log(newDict);
