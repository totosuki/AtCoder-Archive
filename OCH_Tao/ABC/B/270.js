const [X, Y, Z] = require("fs").readFileSync("/dev/stdin", "utf8").trim().split(" ").map(x => parseInt(x, 10));
if ((X > Y && Y > 0 && Z > Y) || (X < Y && Y < 0 && Z < Y)) {
  console.log(-1);
} else if ((X > Y && Y > 0) || (X < Y && Y < 0)) {
  console.log(Math.abs(0 - Z) + Math.abs(X - Z));
} else {
  console.log(Math.abs(X));
}