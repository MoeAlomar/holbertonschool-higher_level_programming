#!/usr/bin/node

const args = process.argv;
if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
}
let i = 0;

while (i < parseInt(args[2])) {
  console.log('X'.repeat(args[2]));
  i++;
}
