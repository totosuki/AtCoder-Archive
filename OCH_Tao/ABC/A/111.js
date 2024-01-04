const N = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let l = [];
for (let i = 0; i < N.length; i++) {
  if (N[i] === "9") {
    l.push("1");
  } else if (N[i] === "1") {
    l.push("9");
  } else {
    l.push(N[i]);
  }
}
console.log(l.join(""));