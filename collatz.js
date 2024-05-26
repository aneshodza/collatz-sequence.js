let calculations = {};

function collatzSequenceLength(n) {
  let length = 1;
  while (n !== 1) {
    if (calculations[n]) {
      length += calculations[n] - 1;
      return length;
    }
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }
    length++;
  }

  return length;
}

const number = parseInt(process.argv[2]);
if (isNaN(number) || number <= 0) {
  console.log('Invalid input. Please enter a positive integer.');
  process.exit(1);
}

console.time('Execution time');

// note down which was the longest
let longest = { number: 0, length: 0 };
for (let i = 1; i <= number; i++) {
  const length = collatzSequenceLength(i);
  calculations[i] = length;
  if (length > longest.length) {
    longest.number = i;
    longest.length = length;
  }
}

console.timeEnd('Execution time');

console.log(`Longest sequence is ${longest.number} with ${longest.length} steps.`);
