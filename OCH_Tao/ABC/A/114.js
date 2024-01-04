const X = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (X === "3" || X === "5" || X === "7") {
  console.log("YES");
} else {
  console.log("NO");
}