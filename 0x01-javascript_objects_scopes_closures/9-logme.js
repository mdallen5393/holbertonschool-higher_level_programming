#!/usr/bin/node
var numPrinted = 0;

exports.logMe = function (item) {
  console.log(numPrinted + ': ' + item);
  numPrinted++;
}
