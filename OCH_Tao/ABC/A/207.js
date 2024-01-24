const L = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
L.sort((a, b) => b - a);
console.log(L[0] + L[1]);