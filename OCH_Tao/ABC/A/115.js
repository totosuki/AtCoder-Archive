const D = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (D === "25") {
  console.log("Christmas");
} else if (D === "24") {
  console.log("Christmas Eve");
} else if (D === "23") {
  console.log("Christmas Eve Eve");
} else {
  console.log("Christmas Eve Eve Eve");
}