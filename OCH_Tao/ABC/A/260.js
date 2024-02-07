const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
let flag = true;
for (let i = 0; i < 3; i++) {
  let cnt = 0;
  for (let j = 0; j < 3; j++) {
    if (S[i] === S[j]) {
      cnt++;
    }
  }
  if (cnt === 1) {
    console.log(S[i]);
    flag = false;
    break;
  }
}
if (flag) {
  console.log(-1);
}