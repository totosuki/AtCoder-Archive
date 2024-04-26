const [X1, Y1, X2, Y2] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
const inc = [X2 - X1, Y2 - Y1];
let rslt = [];
rslt.push(X2 - inc[1]);
rslt.push(Y2 + inc[0]);
rslt.push(rslt[0] - inc[0]);
rslt.push(rslt[1] - inc[1]);
console.log(rslt.join(" "));