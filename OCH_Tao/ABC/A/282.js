const K = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
let tmp = "";
for (let i = 10; i < K + 10; i++) {
  tmp += i.toString(36);
}
console.log(tmp.toUpperCase());