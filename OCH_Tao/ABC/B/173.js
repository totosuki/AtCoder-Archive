const input = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
input.shift();
const S = input.join("");
console.log(`AC x ${(S.match(/AC/g) ?? []).length}`);
console.log(`WA x ${(S.match(/WA/g) ?? []).length}`);
console.log(`TLE x ${(S.match(/TLE/g) ?? []).length}`);
console.log(`RE x ${(S.match(/RE/g) ?? []).length}`);