#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, function (err) {
    if (err) throw err;
  });
});
