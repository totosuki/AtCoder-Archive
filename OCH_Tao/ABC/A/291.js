const S = [...(require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0]];
let cnt = 1;
for (const i of S) {
  if ("A" <= i && i <= "Z") {
    console.log(cnt);
    break;
  } else {
    cnt++;
  }
}