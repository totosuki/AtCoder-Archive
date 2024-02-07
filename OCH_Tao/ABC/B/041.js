const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(BigInt);
console.log(((A * B * C) % BigInt(1e9 + 7)).toString());