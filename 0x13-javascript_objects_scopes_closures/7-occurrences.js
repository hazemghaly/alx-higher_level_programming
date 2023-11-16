#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let h = 0;
  for (h of list) {
    if (h === searchElement) {
      counter++;
    }
  }
  console.log(counter);
};
