const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const O = [...input[0]];
const E = [...input[1]];
let l = [];
for (let i = 0; i < O.length; i++) {
  l.push(O[i]);
  if (O.length > E.length && i === O.length - 1) {
    break;
  } else {
    l.push(E[i]);
  }
}
console.log(l.join(""));