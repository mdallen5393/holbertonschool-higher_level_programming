#!/usr/bin/node
const parsed = parseInt(process.argv[2]);
if (parsed) {
  console.log('My number:', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
