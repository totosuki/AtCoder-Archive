const f = x => {
  if (x === 0) {
    return 1;
  } else {
    return x * f(x - 1);
  }
}
const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
console.log(f(N));