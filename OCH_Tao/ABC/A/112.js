const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n")).map(x => parseInt(x, 10));
if (input[0] === 1) {
  console.log("Hello World");
} else {
  console.log(input[1] + input[2]);
}