const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
const L = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
const X = L.indexOf(S);
console.log(7 - X);