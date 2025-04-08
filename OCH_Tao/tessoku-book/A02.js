const [[, X], [...A]] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n").map(x => x.split(" ").map(y => parseInt(y, 10)));
for (const i of A) {
  if (i === X) {
    console.log("Yes");
    process.exit();
  }
}
console.log("No");