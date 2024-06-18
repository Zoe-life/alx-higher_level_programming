#!/usr/bin/node

exports.esrever = function (list) {
  // Initializing an empty array to store the reversed list
  const reversedList = [];

  // Looping through the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Adding each element from the end of the original list to the reversedList
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};
