#!/usr/bin/node
/*
 *  script that prints all characters of a Star Wars movie:
 *  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 *  Display one character name by line
 *  You must use the Star wars API
 */

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const data = JSON.parse(body).characters;
    for (const index in data) {
      request(data[index], (err, res, body) => {
        if (err) {
          console.log(err);
          return;
        }
        const stars = JSON.parse(body).name;
        console.log(stars);
      });
    }
  }
});
