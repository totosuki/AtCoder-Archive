const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
let A = [...input[0]];
let B = [...input[1]];
let C = [...input[2]];
let i = "a";
while (A.length >= 0 && B.length >= 0 && C.length >= 0) {
  if (i === "a") {
    i = A.shift();
    if (i === undefined) {
      console.log("A");
      break;
    }
  }
  if (i === "b") {
    i = B.shift();
    if (i === undefined) {
      console.log("B");
      break;
    }
  }
  if (i === "c") {
    i = C.shift();
    if (i === undefined) {
      console.log("C");
      break;
    }
  }
}