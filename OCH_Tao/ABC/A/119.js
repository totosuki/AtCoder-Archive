const [Y, M, D] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split("/")).map(x => parseInt(x, 10));
if (M < 5) {
  console.log("Heisei");
} else {
  console.log("TBD");
}