const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const L = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"];
if (L.includes(input.slice(0, 3))) {
  console.log("Yes");
} else if (L.includes(input.slice(1))) {
  console.log("Yes");
} else {
  console.log("No");
}