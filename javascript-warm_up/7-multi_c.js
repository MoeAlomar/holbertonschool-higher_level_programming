#!/usr/bin/node

let i = 0;
const args = process.argv;
if (isNaN(parseInt(args[2]))) {
  console.log('Missing number of occurrences');
}
while (i < parseInt(args[2])) {
  console.log('C is fun');
  i++;
}