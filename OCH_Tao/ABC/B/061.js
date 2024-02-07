const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [N, M] = ((input.shift()).split(" ")).map(x => parseInt(x, 10));
let l = [];
for (let i = 0; i < M; i++) {
  let [a, b] = (input[i].split(" ")).map(x => parseInt(x, 10));
  l.push(a);
  l.push(b);
}
for (let i = 1; i < N + 1; i++) {
  let cnt = 0;
  for (let j = 0; j < l.length; j++) {
    if (l[j] === i) {
      cnt++;
    }
  }
  console.log(cnt);
}