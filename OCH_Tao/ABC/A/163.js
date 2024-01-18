const R = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")), 10);
console.log(2 * R * Math.PI);