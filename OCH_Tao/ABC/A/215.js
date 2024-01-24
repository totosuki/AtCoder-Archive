const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S === "Hello,World!") {
  console.log("AC");
} else {
  console.log("WA");
}