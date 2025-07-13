#!/usr/bin/node

const args = process.argv;
let i = 2;
if (args.length < 4) {
  console.log('0');
} else {
  const array = [];
  while (i < args.length) {
    array.push(parseInt(args[i]));
    i++;
  }
  array.sort(comparer);
  i = array.length - 2;
  console.log(array[i]);
}
function comparer (a, b) {
  return a - b;
}
