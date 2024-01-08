const [A, B] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
if ((A + B) % 2 === 0) {
  console.log(Math.trunc((A + B) / 2));
} else {
  console.log("IMPOSSIBLE");
}