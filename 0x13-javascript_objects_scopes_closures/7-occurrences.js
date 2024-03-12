#!/usr/bin/node
// defines a function that returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(e => e === searchElement).length);
}
