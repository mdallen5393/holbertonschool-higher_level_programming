#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let i = 0; i <= list.length + 3; i++) {
    const last = list.pop();
    newlist.push(last);
  }
  return (newlist);
};
