#!/usr/bin/node
// returns the second largest number

const { argv } = require('process');
if (argv.length <= 3) {
  console.log(0);
} else {
  console.log(argv.sort()[argv.length - 2]);
}
