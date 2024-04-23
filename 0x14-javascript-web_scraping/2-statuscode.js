#!/usr/bin/node
/*
 * script that display the status code of a GET request.
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 */
const request = require('request');
const url = process.argv[2];

request(url, (err, response, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(response.statusCode);
});
