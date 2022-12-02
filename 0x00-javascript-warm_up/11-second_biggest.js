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

// /* PAUL'S METHOD */
// let args = process.argv.slice(2);
// // console.log('only args:', args)
// args = args.map(num => parseInt(num));
// // console.log('parsed:', args)
// args = args.sort();
// // console.log('sorted:', args)
// if (args.length <= 1) {
//   console.log(0);
// } else {
//   console.log(args.slice(-2)[0]);
// }
