const [M, H] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (H % M === 0) {
  console.log("Yes");
} else {
  console.log("No");
}