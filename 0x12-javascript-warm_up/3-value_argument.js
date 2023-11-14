#!/usr/bin/node
const { argv } = require('node:process');
if (!argv[2]) { console.log('No argument'); } else {
  for (let i = 2; s = process.argv[i]; i++) {
    console.log(s);
  }
}
