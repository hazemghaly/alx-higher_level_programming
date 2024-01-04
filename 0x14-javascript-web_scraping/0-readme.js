#!/usr/bin/node
const fs = require('fs');
fs.readFile('cisfun.txt', (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
