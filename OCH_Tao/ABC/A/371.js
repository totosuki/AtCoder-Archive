const [AB, AC, BC] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ");
console.log(AB !== AC ? "A" : AB === BC ? "B" : "C");