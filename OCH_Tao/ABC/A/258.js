const K = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
console.log(`${21 + Math.trunc(K / 60)}:${String(K % 60).padStart(2, "0")}`);