const S = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")[0];
const N = S.length;
if (S === [...S].reverse().join("")) {
  if (S.slice(0, (N - 1) / 2) === [...S.slice(0, (N - 1) / 2)].reverse().join("")) {
    if (S.slice((N + 3) / 2 - 1) === [...S.slice((N + 3) / 2 - 1)].reverse().join("")) {
      console.log("Yes");
    } else {
      console.log("No");
    }
  } else {
    console.log("No");
  }
} else {
  console.log("No");
}