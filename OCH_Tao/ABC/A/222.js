const N = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
console.log(N.padStart(4, "0"));