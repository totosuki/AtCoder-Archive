const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
let cnt = 0;
for (let i = A; i < B + 1; i++) {
  let X = [...String(i)];
  if (String(i) === (X.reverse()).join("")) {
    cnt++;
  }
}
console.log(cnt);