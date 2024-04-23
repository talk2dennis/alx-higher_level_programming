#!/usr/bin/node
/*
 * a script that writes content to a file
 * the first argurment is the file name
 * the second argurment is the content to write
 * */
const fs = require('fs');
const args = process.argv.slice(2);

fs.writeFile(args[0], args[1], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
