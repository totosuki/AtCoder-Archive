const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const L = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "1"];
const A = L.indexOf(input[0]);
const B = L.indexOf(input[1]);
if (A === B) {
  console.log("Draw");
} else if (A > B) {
  console.log("Alice");
} else {
  console.log("Bob");
}