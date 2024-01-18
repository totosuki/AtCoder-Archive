const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const x = [...A].map(x => parseInt(x, 10));
const y = [...B].map(x => parseInt(x, 10));
console.log(Math.max(x[0] + x[1] + x[2], y[0] + y[1] + y[2]));