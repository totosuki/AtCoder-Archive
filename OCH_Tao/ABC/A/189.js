const C = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (C[0] === C[1] && C[1] === C[2]) {
  console.log("Won");
} else {
  console.log("Lost");
}