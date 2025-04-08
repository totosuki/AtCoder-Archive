const STR = [..."BCDEFGHIJKLMNOPQRSTUVWXYZ"];
let cnt = 0;
const S = require("fs").readFileSync("/dev/stdin", "utf8").trim();
let tmp = S.indexOf("A");
for (const i of STR) {
  cnt += Math.abs(tmp - S.indexOf(i));
  tmp = S.indexOf(i);
}
console.log(cnt);