const X = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (X === "1") {
  console.log(0);
} else {
  console.log(1);
}