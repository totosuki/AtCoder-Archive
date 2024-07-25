const R = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
console.log(100 - R % 100);