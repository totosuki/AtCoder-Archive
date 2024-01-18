const [S, T] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const L = ["a", "t", "c", "o", "d", "e", "r"];
let flag = true;
for (let i = 0; i < S.length; i++) {
  if (S[i] === T[i]) {
    continue;
  } else if (S[i] === "@") {
    if (L.includes(T[i])) {
      continue;
    } else {
      flag = false;
    }
  } else if (T[i] === "@") {
    if (L.includes(S[i])) {
      continue;
    } else {
      flag = false;
    }
  } else {
    flag = false;
  }
}
if (flag) {
  console.log("You can win");
} else {
  console.log("You will lose");
}