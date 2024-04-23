#!/usr/bin/node
/*
 * script that prints the title of a Star Wars movie where the episode number matches a given integer.
 *
 * The first argument is the movie ID
 * You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 */
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
