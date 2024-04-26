const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const L = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
console.log(5 - L.indexOf(S));