const [A, B, C] = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
console.log(Number(A + B + C) + Number(B + C + A) + Number(C + A + B));