#!/usr/bin/node
// imports an array and computes a new array.

const initList = require('./100-data').list;
console.log(initList);

const mapList = initList.map((num, index) => {
  return num * index;
});
console.log(mapList);
