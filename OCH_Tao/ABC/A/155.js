const [A, B, C] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
if (A === B && C !== A) {
  console.log("Yes");
} else if (B === C && A !== B) {
  console.log("Yes");
} else if (C === A && B !== C) {
  console.log("Yes");
} else {
  console.log("No");
}