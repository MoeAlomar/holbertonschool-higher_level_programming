#!/usr/bin/node

const args = process.argv;

function factorial (a) {
  if (isNaN(parseInt(a)) || parseInt(a) === 0) {
    return 1;
  }
  return (a * factorial(a - 1));
}
const fact = factorial(args[2]);
console.log(fact);