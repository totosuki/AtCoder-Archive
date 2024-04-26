const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))
const [N, M, X, Y] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
const x = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
const y = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
if (Math.max(...x) < Math.min(...y) && Math.max(...x) > X && Math.min(...y) < Y) {
  console.log("No War");
} else {
  console.log("War");
}