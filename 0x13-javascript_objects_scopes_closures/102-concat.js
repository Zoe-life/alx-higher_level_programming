#!/usr/bin/node

const fs = require('fs'); // Importing the 'fs' module for file system operations

// Getting the file paths from process arguments (excluding the script name)
const fileA = process.argv[2];
const fileB = process.argv[3];
const destination = process.argv[4];

function readFileContent (filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

Promise.all([readFileContent(fileA), readFileContent(fileB)])
  .then((contents) => {
    const combinedContent = contents[0] + contents[1]; // Concatenate contents

    fs.writeFile(destination, combinedContent, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log('Content successfully concatenated and written to:', destination);
      }
    });
  })
  .catch((err) => {
    console.error('Error reading file:', err);
  });
