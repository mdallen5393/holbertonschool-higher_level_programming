#!/usr/bin/node
let nums;
if (process.argv.length < 4) {
  console.log('0');
} else {
  nums = [...process.argv];
  nums = nums.slice(2).map(num => parseInt(num));
  const max = Math.max(...nums);
  nums = nums.filter(num => num !== max);
  console.log(Math.max(...nums));
}
