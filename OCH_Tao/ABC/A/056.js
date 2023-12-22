const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
const A = input[0];
const B = input[1];
if (A === "H") {
  if (B === "H") {
    console.log("H");
  } else {
    console.log("D");
  }
} else {
  if (B === "D") {
    console.log("H");
  } else {
    console.log("D");
  }
}