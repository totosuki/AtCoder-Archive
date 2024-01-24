const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
let l = [];
const x = [/A/g, /B/g, /C/g, /D/g, /E/g, /F/g];
for (let i = 0; i < 6; i++) {
  let tmp = S.matchAll(x[i]);
  l.push([...tmp].length);
}
console.log(l.join(" "));