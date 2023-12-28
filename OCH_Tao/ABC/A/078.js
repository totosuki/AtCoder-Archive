const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const L = ["A", "B", "C", "D", "E", "F"];
if (L.indexOf(input[0]) === L.indexOf(input[1])) {
  console.log("=");
} else if (L.indexOf(input[0]) < L.indexOf(input[1])) {
  console.log("<");
} else {
  console.log(">");
}