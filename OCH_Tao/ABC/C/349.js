const [S, T] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n");
/*  let RE;
  if (T[2] === "X") {
    RE = new RegExp(".*" + T[0] + ".*" + T[1] + ".*$", "i");
  } else {
    RE = new RegExp(".*" + T[0] + ".*" + T[1] + ".*" + T[2] + ".*$", "i");
  }
  if (RE.test(S)) {
    console.log("Yes");
  } else {
    console.log("No");
  }  */
const X = S.toUpperCase() + "X";
const RE = new RegExp([...T].join(".*"));
if (RE.test(X)) {
  console.log("Yes");
} else {
  console.log("No");
}