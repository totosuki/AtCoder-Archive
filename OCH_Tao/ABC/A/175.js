const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S.includes("RRR")) {
  console.log(3);
} else if (S.includes("RR")) {
  console.log(2);
} else if (S.includes("R")) {
  console.log(1);
} else {
  console.log(0);
}