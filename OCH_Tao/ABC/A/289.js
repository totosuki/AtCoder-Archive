const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
let L = "";
for (const i of S) {
  if (i === "0") {
    L += "1";
  } else {
    L += "0";
  }
}
console.log(L);