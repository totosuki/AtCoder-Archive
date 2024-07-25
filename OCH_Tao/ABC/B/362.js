const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
const [xA, yA] = input[0].split(" ").map(x => parseInt(x, 10));
const [xB, yB] = input[1].split(" ").map(x => parseInt(x, 10));
const [xC, yC] = input[2].split(" ").map(x => parseInt(x, 10));
const AB = (xA - xB) ** 2 + (yA - yB) ** 2;
const BC = (xB - xC) ** 2 + (yB - yC) ** 2;
const CA = (xC - xA) ** 2 + (yC - yA) ** 2;
if (AB + BC === CA || BC + CA === AB || CA + AB === BC) {
  console.log("Yes");
} else {
  console.log("No");
}