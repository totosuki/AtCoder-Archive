const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
let l = [];
for (let i = 0; i < S.length; i++) {
  if (S[i] === "B") {
    l.pop();
  } else {
    l.push(S[i]);
  }
}
console.log(l.join(""));