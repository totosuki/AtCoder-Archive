const [A, B, C] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if ((A <= B && B <= C) || (C <= B && B <= A)) {
  console.log("Yes");
} else {
  console.log("No");
}