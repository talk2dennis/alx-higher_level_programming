#!/usr/bin/node
/*
 * script that prints the number of movies where the character “Wedge Antilles” is present.
 *
 * The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 */

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const res in data) {
      const characters = data[res].characters;
      for (const id in characters) {
        if (characters[id].includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
