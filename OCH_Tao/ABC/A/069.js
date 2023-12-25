const NM = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
console.log((NM[0] - 1) * (NM[1] - 1));