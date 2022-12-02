#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const elem in list) {
    if (list[elem] === searchElement) {
      count++;
    }
  }
  return (count);
};
