const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
for (let i = N; i > -1; i--) {
  console.log(i);
}