const hon = ["2", "4", "5", "7", "9"];
const pon = ["0", "1", "6", "8"];
const N = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (hon.includes(N[N.length - 1])) {
  console.log("hon");
} else if (pon.includes(N[N.length - 1])) {
  console.log("pon");
} else {
  console.log("bon");
}