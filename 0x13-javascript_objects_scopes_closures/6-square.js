#!/usr/bin/node
// defines square class that inherits from the rectangular class

const SquareBase = require('./5-square');

class Square extends SquareBase {

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
