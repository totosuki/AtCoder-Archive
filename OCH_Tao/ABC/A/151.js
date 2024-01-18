const C = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let x = C.charCodeAt(0);
console.log(String.fromCharCode(x + 1));