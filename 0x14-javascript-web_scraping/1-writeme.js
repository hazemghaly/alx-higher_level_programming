#!/usr/bin/node
const fs = require('fs');
// Write data in 'Output.txt' .
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  // In case of a error throw err.
  if (err) throw err;
});
