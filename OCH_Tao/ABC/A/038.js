const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (input.charAt(input.length - 1) === "T") {
  console.log("YES");
} else {
  console.log("NO");
}