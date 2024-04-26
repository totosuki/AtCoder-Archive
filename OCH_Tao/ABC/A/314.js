const P = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
const N = parseInt(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0], 10);
console.log(P.slice(0, N + 2));