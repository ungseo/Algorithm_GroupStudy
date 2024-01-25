const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.once("line", (line) => {
  const [A, B] = line.split(' ').map(Number);
  console.log(A+B);
  rl.close();
});