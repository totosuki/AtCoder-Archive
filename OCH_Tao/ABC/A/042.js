const input = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ");
let cnt5 = 0;
let cnt7 = 0;
for (let i = 0; i < input.length; i++) {
  if (input[i] === "5") {
    cnt5++;
  } else if (input[i] === "7") {
    cnt7++;
  }
}
if (cnt5 === 2 && cnt7 == 1) {
  console.log("YES");
} else {
  console.log("NO");
}