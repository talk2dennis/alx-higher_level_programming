#!/usr/bin/node
// defines a rectangle class with features

class Rectangle {
  constructor (w, h) {
    // creates an empty class if w or h <= 0
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // method that rotates the rectangle
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // method that doubles the size of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
