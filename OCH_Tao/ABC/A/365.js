const Y = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim(), 10);
console.log(Y % 400 === 0 ? 366 : Y % 100 === 0 ? 365 : Y % 4 === 0 ? 366 : 365);