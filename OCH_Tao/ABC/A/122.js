const B = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (B === "A") {
  console.log("T");
} else if (B === "T") {
  console.log("A");
} else if (B === "C") {
  console.log("G");
} else {
  console.log("C");
}