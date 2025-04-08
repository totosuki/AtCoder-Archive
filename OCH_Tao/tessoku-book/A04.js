const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
console.log(N.toString(2).padStart(10, "0"));