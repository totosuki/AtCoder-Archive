const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const ABCDE = ["A", "B", "C", "D", "E"];
const same = (element) => element === input[0];
console.log((ABCDE.findIndex(same)) + 1);