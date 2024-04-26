let [R, D, X] = ((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0].split(" ")).map(x => parseInt(x, 10));
for (let i = 0; i < 10; i++) {
  X = R * X - D;
  console.log(X);
}