const [N, A, B] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0].split(" ").map(BigInt);
console.log(((N / (A + B)) * A + (N % (A + B) < A ? N % (A + B) : A)).toString());