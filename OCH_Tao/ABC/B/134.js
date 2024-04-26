const [N, D] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
console.log(Math.ceil(N / (2 * D + 1)));