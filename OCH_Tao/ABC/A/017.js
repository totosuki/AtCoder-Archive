const input = require("fs").readFileSync("/dev/stdin", "utf8").split("\n");
const S1 = input[0].split(" ");
const S2 = input[1].split(" ");
const S3 = input[2].split(" ");
let score = 0
score += parseInt(S1[0], 10) * parseInt(S1[1], 10) / 10;
score += parseInt(S2[0], 10) * parseInt(S2[1], 10) / 10;
score += parseInt(S3[0], 10) * parseInt(S3[1], 10) / 10;
console.log(score);