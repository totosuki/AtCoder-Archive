const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const [R, C] = (input[0].split(" ")).map(x => parseInt(x, 10));
const A1 = (input[1].split(" ")).map(x => parseInt(x, 10));
const A2 = (input[2].split(" ")).map(x => parseInt(x, 10));
if (R === 1) {
  if (C === 1) {
    console.log(A1[0]);
  } else {
    console.log(A1[1]);
  }
} else {
  if (C === 1) {
    console.log(A2[0]);
  } else {
    console.log(A2[1]);
  }
}