#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (num) {
  console.log(Array(num).fill('C is fun').join('\n'));
}
