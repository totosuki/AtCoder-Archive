const [A, B, w] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(x => parseInt(x, 10));
const W = w * 1000;
if (Math.floor(W / A) !== Math.floor(W / B)) {
  console.log(`${Math.ceil(W / B)} ${Math.floor(W / A)}`);
} else {
  if (W % A > B - A || W % B > B - A) {
    console.log("UNSATISFIABLE");
  } else {
    console.log(`${Math.floor(W / A)} ${Math.floor(W / B)}`);
  }
}