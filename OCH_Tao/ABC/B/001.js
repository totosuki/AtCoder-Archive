const M = parseInt((require("fs").readFileSync("/dev/stdin", "utf8").trim().split("\n"))[0], 10);
const km = M / 1000;
if (km < 0.1) {
  console.log("00");
} else if (0.1 <= km && km <= 5) {
  if (String(10 * km).length === 1) {
    console.log("0" + Math.trunc(10 * km));
  } else {
    console.log(10 * km);
  }
} else if (6 <= km && km <= 30) {
  console.log(km + 50);
} else if (35 <= km && km <= 70) {
  console.log((km - 30) / 5 + 80);
} else {
  console.log(89);
}