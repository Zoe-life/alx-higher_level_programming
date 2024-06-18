#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  let counter = 0;

  function innerFunction () {
    counter++;
    theFunction(counter);
  }

  for (let i = 0; i < number; i++) {
    innerFunction();
  }
}

module.exports = { addMeMaybe };
