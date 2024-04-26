const W = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[1].split(" ");
const X = ["and", "not", "that", "the", "you"];
for (let i = 0; i < 5; i++) {
  if (W.includes(X[i])) {
    console.log("Yes");
    break;
  }
  if (i === 4) {
    console.log("No");
  }
}