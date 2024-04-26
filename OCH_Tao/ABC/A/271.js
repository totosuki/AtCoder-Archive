const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
console.log(N.toString(16).padStart(2, "0").toUpperCase());