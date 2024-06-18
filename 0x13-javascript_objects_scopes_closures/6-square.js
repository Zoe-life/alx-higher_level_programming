#!/usr/bin/node

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char = 'X') {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += char;
        }
        console.log(line);
      }
    } else {
      console.log('Square is empty');
    }
  }
}

module.exports = Square;
