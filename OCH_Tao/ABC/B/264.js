const [R, C] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
let X = [[true]];
for (let i = 0; i < 7; i++) {
  if (i % 2 === 0) {
    X = X.map(x => [].concat(false, ...x, false));
    const tmp = new Array(X[0].length).fill(false);
    X.unshift(tmp);
    X.push(tmp);
  } else {
    X = X.map(x => [].concat(true, ...x, true));
    const tmp = new Array(X[0].length).fill(true);
    X.unshift(tmp);
    X.push(tmp);
  }
}
console.log(X[R - 1][C - 1] ? "white" : "black");