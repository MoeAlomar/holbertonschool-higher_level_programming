#!/usr/bin/node
const args = process.argv;

function add (a, b) {
  if (isNaN(parseInt(a)) || isNaN(parseInt(b))) {
    return NaN;
  }
  return parseInt(a) + parseInt(b);
}
const sum = add(args[2], args[3]);
console.log(sum);