const [N, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let l = [];
for (let i = 0; i < 50; i++) {
  if (i === 0) {
    l.push("b");
  } else if (i % 3 === 1) {
    l.push(`a${l[l.length - 1]}c`);
  } else if (i % 3 === 2) {
    l.push(`c${l[l.length - 1]}a`);
  } else {
    l.push(`b${l[l.length - 1]}b`);
  }
}
console.log(l.indexOf(S));