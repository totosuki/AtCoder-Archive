const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (input[1] - input[0] === input[2] - input[1]) {
  console.log("YES");
} else {
  console.log("NO");
}