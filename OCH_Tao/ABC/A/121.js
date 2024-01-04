const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [H, W] = (input[0].split(" ")).map(x => parseInt(x, 10));
const [h, w] = (input[1].split(" ")).map(x => parseInt(x, 10));
console.log((H - h) * (W - w));