const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let l = [0, 0, 0, 1];
for (let i = 0; i < N; i++) {
  l.push((l[1] + l[2] + l[3]) % 10007);
  l.splice(0, 1);
}
console.log(l[0]);