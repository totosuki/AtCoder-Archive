const [input, S] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
let [N, K] = input.split(" ").map(x => parseInt(x, 10));
let ans = "";
for (let i = 0; i < N; i++) {
  if (S[i] === "o" && K > 0) {
    ans += "o";
    K--;
  } else {
    ans += "x";
  }
}
console.log(ans);