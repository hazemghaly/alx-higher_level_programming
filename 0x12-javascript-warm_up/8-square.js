#!/usr/bin/node
if (!process.argv[2]) { console.log('Missing size'); } else {
  if (isNaN(Number(process.argv[2]))) {
    console.log('Missing size');
  }
}
for (let i = 1; i <= process.argv[2]; i++) {
  let line = '';
  for (let j = 1; j <= process.argv[2]; j++) {
    line += 'X';
  }
  console.log(line);
}
