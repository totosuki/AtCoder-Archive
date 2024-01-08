const S = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0];
if (S === "Sunny") {
  console.log("Cloudy");
} else if (S === "Cloudy") {
  console.log("Rainy");
} else {
  console.log("Sunny");
}