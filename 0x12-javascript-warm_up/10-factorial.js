#!/usr/bin/node
// factorial using recursion

const { argv } = require('process');

function factorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(parseInt(argv[2])));
