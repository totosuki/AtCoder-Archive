const T = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
const f = x => x ** 2 + 2 * x + 3;
console.log(f(f(f(T) + T) + f(f(T))));