const [N, S, T] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let flag = true;
for (let i = 0; i < parseInt(N, 10); i++) {
  if (S[i] === T[i]) {
    continue;
  } else if (["1", "l"].includes(S[i]) && ["1", "l"].includes(T[i])) {
    continue;
  } else if (["0", "o"].includes(S[i]) && ["0", "o"].includes(T[i])) {
    continue;
  } else {
    console.log("No");
    flag = false;
    break;
  }
}
if (flag) {
  console.log("Yes");
}