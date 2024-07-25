const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const K = parseInt(input[0].split(" ")[1], 10);
const H = input[1].split(" ").map(x => parseInt(x, 10));
console.log(H.filter(x => x >= K).length);