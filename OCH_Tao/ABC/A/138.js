const [input, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
const A = parseInt(input, 10);
if (A < 3200) {
  console.log("red");
} else {
  console.log(S);
}