const [V, T, S, D] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (V * T <= D && D <= V * S) {
  console.log("No");
} else {
  console.log("Yes");
}