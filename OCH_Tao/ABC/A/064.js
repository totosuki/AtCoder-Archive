const input = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if ((input[1] * 10 + input[2]) % 4 === 0) {
  console.log("YES");
} else {
  console.log("NO");
}