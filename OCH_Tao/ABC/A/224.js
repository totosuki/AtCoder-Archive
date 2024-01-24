const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S.slice(S.length - 2) === "er") {
  console.log("er");
} else {
  console.log("ist");
}