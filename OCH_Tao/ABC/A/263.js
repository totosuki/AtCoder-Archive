const L = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
L.sort((a, b) => a - b);
if ((L[0] === L[2] && L[3] === L[4]) || (L[0] === L[1] && L[2] === L[4])) {
  console.log("Yes");
} else {
  console.log("No");
}