#!/usr/bin/node
function findSecondLargestElem (arr) {
  let first = 0; let second = 0;
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] > first) {
      second = first;
      first = arr[i];
    } else if (arr[i] > second && arr[i] !== first) {
      second = arr[i];
    }
  }
  console.log(second);
}
const arr = process.argv;
findSecondLargestElem(arr);
