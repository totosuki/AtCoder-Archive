let N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
const hh = String(Math.trunc(N / 3600)).padStart(2, "0");
N = N % 3600;
const mm = String(Math.trunc(N / 60)).padStart(2, "0");
N = N % 60;
const ss = String(N).padStart(2, "0");
console.log(`${hh}:${mm}:${ss}`);