const N = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
if (N < 42) {
  console.log("AGC" + String(N).padStart(3, "0"));
} else {
  console.log("AGC" + String(N + 1).padStart(3, "0"));
}