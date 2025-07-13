#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined) {
  console.log('Not a number');
} else if (parseInt(args[2])) {
  console.log('My number: ' + args[2]);
} else {
  console.log('Not a number');
}