#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w)) {
      this.width = w;
    } else {
      this.width = undefined;
    }

    if (Number.isInteger(h)) {
      this.height = h;
    } else {
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
