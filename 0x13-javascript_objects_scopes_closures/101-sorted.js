#!/usr/bin/node
const dict = require('./101-data.js').dict;
let nD = {};
for (let key in dict) {
  if (nD[dict[key]] === undefined) {
    nD[dict[key]] = [key];
  } else {
    nD[dict[key]].push(key);
  }
}
console.log(nD);
