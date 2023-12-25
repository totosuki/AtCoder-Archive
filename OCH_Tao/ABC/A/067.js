const AB = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if (AB[0] % 3 === 0) {
  console.log("Possible");
} else if (AB[1] % 3 === 0) {
  console.log("Possible");
} else if ((AB[0] + AB[1]) % 3 === 0) {
  console.log("Possible");
} else {
  console.log("Impossible");
}