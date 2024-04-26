const N = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const MMYY = parseInt(N.slice(0, 2), 10) < 13 && N.slice(0, 2) !== "00";
const YYMM = parseInt(N.slice(2), 10) < 13 && N.slice(2) !== "00";
if (MMYY && YYMM) {
  console.log("AMBIGUOUS");
} else if (MMYY) {
  console.log("MMYY");
} else if (YYMM) {
  console.log("YYMM");
} else {
  console.log("NA");
}