#!/usr/bin/node
/*
 * script that computes the number of tasks completed by user id.
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 */
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  if (res.statusCode === 200) {
    const todos = {};
    const data = JSON.parse(body);
    for (const index in data) {
      const result = data[index];
      if (result.completed) {
        if (todos[result.userId] !== undefined) {
          todos[result.userId]++;
        } else {
          todos[result.userId] = 1;
        }
      }
    }
    console.log(todos);
  }
});
