const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, Q] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let x = new Array(N).fill(0);
for (let i = 0; i < Q; i++) {
  let [l, r, t] = (input[i].split(" ")).map(x => parseInt(x, 10));
  x.fill(t, l - 1, r);
}
console.log(x.join("\n"));