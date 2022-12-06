#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (err, response, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
