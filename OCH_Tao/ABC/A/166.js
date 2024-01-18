const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S === "ABC") {
  console.log("ARC");
} else {
  console.log("ABC");
}