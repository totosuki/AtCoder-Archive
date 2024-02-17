const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const N = parseInt(input, 10);
const fx = ([...input].map(x => parseInt(x, 10))).reduce((a, b) => a + b);
if (N % fx === 0) {
  console.log("Yes");
} else {
  console.log("No");
}