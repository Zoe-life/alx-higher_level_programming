#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0) {
      this.width = w;
    } else {
      this.width = undefined;
      this.height = undefined;
    }

    if (this.width !== undefined && Number.isInteger(h) && h > 0) {
      this.height = h;
    }
  }
}

module.exports = Rectangle;
