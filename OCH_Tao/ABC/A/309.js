const [A, B] = (require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ").map(x => parseInt(x, 10));
if (A % 3 !== 0 && A + 1 === B) {
  console.log("Yes");
} else {
  console.log("No");
}