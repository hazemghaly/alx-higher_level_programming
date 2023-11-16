#!/usr/bin/node
exports.esrever = function (list) {
  const rrl = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rrl.push(list[i]);
  }
  return (rrl);
};
