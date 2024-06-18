#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0) {
      this.width = w;
    } else {
      this.width = undefined;
    }

    if (Number.isInteger(h) && h > 0) {
      this.height = h;
    } else {
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
