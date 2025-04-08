/*
const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log((S.indexOf("R") < S.indexOf("K") && S.indexOf("K") < S.lastIndexOf("R")) && (S.indexOf("B") % 2 !== S.lastIndexOf("B") % 2) ? "Yes" : "No");
*/
const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
console.log(/R.*K.*R/.test(S) && /B(..)*B/.test(S) ? "Yes" : "No");