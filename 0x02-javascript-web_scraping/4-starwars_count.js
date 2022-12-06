#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) throw err;
  const data = JSON.parse(body).results;
  let count = 0;
  for (const movie in data) {
    const chars = data[movie].characters;
    // console.log(JSON.parse(body).title)
    for (const char in chars) {
      if (chars[char].includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
