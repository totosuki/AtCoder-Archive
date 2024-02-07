const W = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const X = [...new Set([...W])];
let re = [];
for (let i = 0; i < X.length; i++) {
  re.push(new RegExp(X[i], "g"));
}
let flag = true;
for (let i = 0; i < X.length; i++) {
  if ([...W.matchAll(re[i])].length % 2 !== 0) {
    flag = false;
    break;
  }
}
if (flag) {
  console.log("Yes");
} else {
  console.log("No");
}