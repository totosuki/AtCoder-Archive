const [, S] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"));
if (/\|.*\*.*\|/.test(S)) {
  console.log("in");
} else {
  console.log("out");
}