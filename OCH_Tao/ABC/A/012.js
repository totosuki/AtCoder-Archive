const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const AB = input[0].split(" ");
console.log(AB[1] + " " + AB[0]);