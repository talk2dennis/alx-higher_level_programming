#!/usr/bin/node
// defines an empty rectangle class

class Rectangle {
  constructor (w, h) {
    // creates an empty class if w or h <= 0
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
