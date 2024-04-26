const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
for (let i = 0; i < B - A; i++) {
  cnt += i;
}
console.log(cnt - A);