#!/usr/bin/node
// defines square class that inherits from the rectangular class

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
