#!/usr/bin/node
function fact (a) {
  if (NaN) {
    return (1);
  }
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(Number(process.argv[2])));
