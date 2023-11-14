#!/usr/bin/node
const { argv, exit } = require('node:process');
if (!argv[2]) {
  console.log('No argument');
  exit();
}
let i = 2;
if (!argv[i]) {
  exit();
}
while (argv[i]); {
  console.log(process.argv[i]);
  i++;
}
