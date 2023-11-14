#!/usr/bin/node
const { argv, exit } = require('node:process');
let i = 2;
if (!argv[2]) {
  console.log('undefined is undefined \r');
}
while (argv[i]) {
  if (!argv[2]) {
    console.log(' is undefined \r');
  } else {
    i++;
    console.log('%s is %s \r', argv[2], argv[i]);
  }
  i++;
  if (!argv[i]) {
    exit();
  }
}
